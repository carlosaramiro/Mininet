from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink

class MyTopo( Topo ):
    "Simple topology example."

    def build( self, core=1, aggregation=2, edge=2, h=1):
        "Create custom topo."
        Core= [core]
        Aggr= [aggregation]
        Edge=[edge]
        Host=[edge*h]
	self
        # Add hosts and switches
        "Creating Core Switches"
        for i in range(core):
                Core.append(self.addSwitch('s%s' % i))
                print(Core[i+1])

        "Creating Aggregation Switches"
        for i in range(aggregation):
                Aggr.append(self.addSwitch('s%s' % (i+core)))

        "Creating Edge Switches"
        for i in range(edge):
                Edge.append(self.addSwitch('s%s' % (i+core+aggregation)))        
	
	"Creating Hosts"
        for i in range (h*edge):
                Host.append(self.addHost('h%s' % i))

        # Add links
	a=0        

        """for i in range (core):
                for j in range (aggregation):
                        self.addLink( Core[i+1], Aggr[j+1], bw=10, delay='5ms')
			for k in range (edge):
				self.addLink(Aggr[j+1], Edge[k+1], bw=10, delay= '5ms')
				for n in range (h*edge):
					self.addLink(Edge[k+1], Host[n+1])"""
	self.addLink('s0','s1')
	self.addLink('s0','s2')
	self.addLink('s1','s3')
	self.addLink('s2','s4')
	self.addLink('s3','h1')
	self.addLink('s4','h1')
        self.addLink('s3','h0')
        self.addLink('s4','h0')

				
				
        
topos= { 'mytopo': ( lambda: MyTopo() ) }
