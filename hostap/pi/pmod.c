#include <linux/netdevice.h>
#include <linux/skbuff.h>
#include <linux/ip.h>
#include <net/sock.h>

struct packet_type my_proto;

int packet_interceptor(struct sk_buff *skb,
                       struct net_device *dev,
                       struct packet_type *pt,
                       struct net_device *orig_dev) {
    
    printk(KERN_INFO "pmod intercepted, len=%ud\n", skb->len);
    
    return 0;
}

static int pmo_init( void ) {
   printk(KERN_INFO "Hello, world!\n");
   
   my_proto.type = htons(ETH_P_ALL);
   my_proto.dev = NULL;
   my_proto.func = packet_interceptor;
   
   dev_add_pack(&my_proto);
   return 0;
}    

static void pmo_exit(void) {
    dev_remove_pack(&my_proto);
    printk(KERN_INFO "Bye, world\n");
}

module_init(pmo_init);
module_exit(pmo_exit);
