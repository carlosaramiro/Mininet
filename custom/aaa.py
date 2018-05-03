#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

	net = Mininet( topo=None,
		build=False,
		ipBase='10.0.0.0/8')
	core=1
	aggregation=2
	edge=2
	h=1
	Core=[core]
	Aggr= [aggregation]
	Edge=[edge]
	Host= [edge*h]



	info( '*** Adding controller\n' )
	c0=net.addController(name='c0',
		controller=Controller,
                protocol='tcp',
                port=6633)

	info( '*** Add switches\n')
        "s14 = net.addSwitch('s14', cls=OVSKernelSwitch)"
        for i in range(core):
    		Core.append(net.addSwitch('s%s' % i))

        for i in range(aggregation):
    		Aggr.append(net.addSwitch('s%s' % (i+core)))

        for i in range(edge):
    		Edge.append(net.addSwitch('s%s' % (i+core+aggregation), cls=OVSKernelSwitch))

    

        info( '*** Add hosts\n')
        "h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)"
    
        for i in range (h*edge):
    		Host.append(net.addHost('h%s' % i))


        info( '*** Add links\n')
        for i in range (core):
    		for j in range (aggregation):
    			net.addLink( Core[i+1], Aggr[j+1])
    			for k in range (edge):
    				net.addLink(Aggr[j+1], Edge[k+1])
                                for n in range (h*edge):
                                	net.addLink(Edge[k+1], Host[n+1])
   


	info( '*** Starting network\n')
        net.build()
        info( '*** Starting controllers\n')
        for controller in net.controllers:
        	controller.start()

        info( '*** Starting switches\n')
        net.get('s4').start([])
        net.get('s3').start([])
        net.get('s2').start([])
        net.get('s1').start([])
        net.get('s0').start([c0])

        info( '*** Post configure switches and hosts\n')

        CLI(net)
        net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
        myNetwork()

