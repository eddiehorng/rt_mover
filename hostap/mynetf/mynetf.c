#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <net/tcp.h>
void ip_itoa(unsigned ipAddr, char *ip_str)
{
    unsigned short a, b, c, d;
    a = (ipAddr & (0xff << 24)) >> 24;
    b = (ipAddr & (0xff << 16)) >> 16;
    c = (ipAddr & (0xff << 8)) >> 8;
    d = ipAddr & 0xff;
    sprintf(ip_str, "%hu.%hu.%hu.%hu", d, c, b, a);
}    

static unsigned int posthook_fn(struct sk_buff *skb)
{
    struct iphdr *iph;
    struct tcphdr *tcph;
    iph = ip_hdr(skb);
    tcph = (struct tcphdr *)(skb->data + iph->ihl * 4);
    unsigned int tcplen;
    
    struct iphdr* ip_header = ip_hdr(skb);
    
    //tcph->source = port;
    //iph->saddr = addr;
    
    int len = skb->len;
    tcph->check = 0;
    tcph->check = tcp_v4_check(len - 4*iph->ihl,
                             iph->saddr, iph->daddr,
                             csum_partial((char *)tcph, len-4*iph->ihl,
                                          0));
    
    //tcplen = (skb->len - (ip_header->ihl << 2));
    //tcph->check = 0; 
    //tcp_checksum_complete(skb);
    /*
    tcph->check = tcp_v4_check(tcph, tcplen, 
                               iph->saddr, 
                               iph->daddr, 
                               csum_partial((char *)tcph, tcplen, 0)); 
                               */
    //skb->ip_summed = CHECKSUM_NONE; //stop offloading
        
    ip_header->check = 0;
    ip_header->check = ip_fast_csum((u8 *)iph, iph->ihl);         

    return NF_ACCEPT;
}

void mod_package(struct sk_buff *skb)
{
    struct iphdr *ip = 0;
    struct tcphdr *tcp = 0;
    unsigned char *user_data = 0; 
    unsigned char *tail = 0;
    int datasize =0;
    
    if ( skb )
    {
        ip = (struct iphdr *)skb_network_header(skb);
        if (ip && ip->protocol == IPPROTO_TCP)
        {
            skb_set_transport_header(skb, ip->ihl * 4);
            tcp = (struct tcphdr *)skb_transport_header(skb);
            
            //if ( tcp && tcp->dest == htons(63947))
            {               
                if (tcp->syn)
                {
                    //printk(KERN_INFO "Connect %d\r\n", ip->saddr);
                }
                else if (tcp->fin || tcp->rst)
                {
                    //printk(KERN_INFO "Disconnect %d\r\n", ip->saddr);
                }
                else
                {
                    user_data = (unsigned char *)((unsigned char *)tcp + (tcp->doff * 4));
                    tail = skb_tail_pointer(skb);
                    if( user_data && tail )
                    {
                        datasize = (int)((long)tail-(long)user_data);
                        if( datasize > 0 )
                        {
                            
                            char ipstr1[40], ipstr2[40];
                            ip_itoa(ip->saddr, ipstr1);
                            ip_itoa(ip->daddr, ipstr2);
                            //strncpy(buf, user_data, datasize);
                            // datasize is 1460!
                            //printk(KERN_INFO "mynetf, ip(%d)\n", datasize);
                            //printk(KERN_INFO "mynetf, %s (%u) -> %s (%u), len=%u\n", ipstr1, ip->saddr, ipstr2, ip->daddr, skb->len);
                            //printk(KERN_INFO "mynetf, cmp=%d\n", memcmp(user_data, "hello", datasize));
                            if(datasize==9) { 
                                char *pattern = "\x04\x00\x29\x13\x00";
                                if(memcmp(user_data, (void *)pattern, 5)==0) {
                                    printk(KERN_INFO "mynetf, going to mod package content! %x:%x:%x:%x:%x\n"
                                    , user_data[0], user_data[1], user_data[2], user_data[3], user_data[4]);
                                    user_data[5]=0xb9;
                                    user_data[6]=0x66;
                                    posthook_fn(skb);
                                }
                            }
                            if(datasize==34) { 
                                char *pattern = "\x1d\x00\x2b\x13\x00\x01";
                                if(memcmp(user_data, (void *)pattern, 6)==0) {
                                    printk(KERN_INFO "mynetf, going to mod package content2! %x:%x:%x:%x:%x\n"
                                    , user_data[0], user_data[1], user_data[2], user_data[3], user_data[4]);
                                    user_data[6]=0xb9;
                                    user_data[7]=0x66;
                                    posthook_fn(skb);
                                }
                            }
                            /*
                            if(ip->saddr==198917074) {
                                printk(KERN_INFO "mynetf, going to mod package content!(test)\n");
                                user_data[0]='X';
                                user_data[1]='X';
                            }
                            */
                        }
                    }
                }
            }
        }
    }
        
}



// Handler function
static unsigned int my_handler(const struct nf_hook_ops *ops,
                              struct sk_buff *skb,
                              const struct net_device *in,
                              const struct net_device *out,
                              int (*okfn)(struct sk_buff *))
{
    struct iphdr* iph = ip_hdr(skb);
    char ipstr1[40], ipstr2[40];
    ip_itoa(iph->saddr, ipstr1);
    ip_itoa(iph->daddr, ipstr2);
    
    //printk(KERN_INFO "mynetf, %s (%u) -> %s (%u), len=%u\n", ipstr1, iph->saddr, ipstr2, iph->daddr, skb->len);
    
    mod_package(skb);
    
    return NF_ACCEPT;
    // or
    //return NF_DROP;
}

// Handler registering struct
static struct nf_hook_ops my_hook __read_mostly = {
    .hook = my_handler,
    .pf = NFPROTO_IPV4,
    //.hooknum = (1 << NF_INET_PRE_ROUTING),
    .priority = NF_IP_PRI_FIRST // My hook will be run before any other netfilter hook
};

static int my_init(void) {
    int err = nf_register_hook (&my_hook);
    if (err) {
        printk (KERN_ERR "Could not register hook\n");
    }
    return err;
}

static void my_exit(void) {
    nf_unregister_hook(&my_hook);
    printk(KERN_INFO "Bye, mfnetf\n");
}

module_init(my_init);
module_exit(my_exit);