#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <linux/if.h>
#include <linux/sockios.h>
#include <stdint.h>
#include <stdbool.h>

#define MAC_SIZE 6
#define ARPHRD_ETHER 1

typedef struct s_mac
{
    uint8_t addr[MAC_SIZE];
} Mac;

bool chmac(const char *iface, Mac mac);
Mac generatemac(void);
void print_mac(Mac mac);

Mac generatemac()
{
    Mac mac;
    mac.addr[0] = (uint8_t)(rand() % 256) & 0xFE;
    mac.addr[1] = (uint8_t)(rand() % 256);
    mac.addr[2] = (uint8_t)(rand() % 256);
    mac.addr[3] = (uint8_t)(rand() % 256);
    mac.addr[4] = (uint8_t)(rand() % 256);
    mac.addr[5] = (uint8_t)(rand() % 256);
    return mac;
}

void print_mac(Mac mac)
{
    printf("Generated MAC Address: %02x:%02x:%02x:%02x:%02x:%02x\n",
           mac.addr[0], mac.addr[1], mac.addr[2],
           mac.addr[3], mac.addr[4], mac.addr[5]);
}

bool chmac(const char *iface, Mac mac)
{
    struct ifreq ifr;
    int sockfd;

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0)
    {
        perror("socket");
        return false;
    }

    strncpy(ifr.ifr_name, iface, IFNAMSIZ - 1);
    ifr.ifr_name[IFNAMSIZ - 1] = '\0';

    memcpy(ifr.ifr_hwaddr.sa_data, mac.addr, MAC_SIZE);
    ifr.ifr_hwaddr.sa_family = ARPHRD_ETHER;

    if (ioctl(sockfd, SIOCSIFHWADDR, &ifr) < 0)
    {
        perror("ioctl(SIOCSIFHWADDR)");
        close(sockfd);
        return false;
    }

    close(sockfd);
    return true;
}

int main(int argc, char *argv[])
{
    Mac mac;

    if (argc < 2)
    {
        fprintf(stderr, "Usage: %s INTERFACE\n", argv[0]);
        return -1;
    }

    const char *iface = argv[1];

    srand((unsigned int)getpid());
    mac = generatemac();
    print_mac(mac);

    if (chmac(iface, mac))
    {
        printf("MAC address successfully changed on interface %s\n", iface);
    }
    else
    {
        fprintf(stderr, "Failed to change MAC address on interface %s\n", iface);
        return -1;
    }

    return 0;
}
