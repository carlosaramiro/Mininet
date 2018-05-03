from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
from mininet.node import Controller

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self, core=3, aggregation=6, edge=9, h=2, **opts):
        "Create custom topo."
	Core= [core]
	Aggr= [aggregation]
	Edge=[edge]
	self.Host=[edge*h]

	"Topo.__init__(self)"
	super(MyTopo, self).__init__(**opts)

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
                self.Host.append(self.addHost('h%s' % i)) 

        # Add links
	"Links between Core and Aggregation Switches: All connected"
        for i in range (core):
                for j in range (aggregation):
                        self.addLink( Core[i+1], Aggr[j+1], bw=10, delay='5ms')			

	"""LInks between Aggregation and Edge Switches: We make groups depending on 
	the number of core switches"""
	n=0
	m=0
	for k in range (core):
		for i in range(n,aggregation/core+n):
			for j in range (m, edge/core+m):
				self.addLink(Aggr[i+1], Edge[j+1], bw=10, delay='5ms')
		n=n+aggregation/core
		m=m+edge/core
	
	n=0
	"""Links between Edge Switches and hosts: h hosts for each Swith"""
	for i in range (edge):
		for j in range(n,h+n):
			self.addLink(Edge[i+1], self.Host[j+1], bw=10, delay='5ms')
			
		n=n+2
	
	def hosts(n=1):
		return self.Host[n]

topos = { 'mytopo': MyTopo }
print("Ha terminado")

