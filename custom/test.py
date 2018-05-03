from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink

class MyTopo( Topo ):
    "Simple topology example."

    def build( self, n=2, h=4 ):
        "Create custom topo."
	Switch= [n]
	Host= [h]
        # Add hosts and switches
        for i in range(n):
                Switch.append(self.addSwitch('s%s' % i))

        for i in range (h):
                Host.append(self.addHost('h%s' % i)) 

        # Add links
        for i in range (n):
                for j in range (h):
                        self.addLink( Switch[i+1], Host[j+1], bw=15, delay='10ms')


topos = { 'mytopo': ( lambda: MyTopo() ) }




