import unittest 
import sys 
import time
import os
import random
import thread
sys.path.append('.')
from mininet.net import Mininet
from mininet.node import Ryu, OVSSwitch
from mininet.node import Host
from mininet.clean import cleanup
from mininet.link import TCLink
from mininet.cli import CLI
from datacenter_tier3 import MyTopo



class testSwitchTopo(object):
	"Test ping with the specified topology"
	topoClass = None # Override with topology
	ryuParams = ['ryu.app.simple_switch_13']
	mayDrop = 0
	top=MyTopo(2, 2, 4, 2)

	def controller(self, name, **params):
		return Ryu(name, *self.ryuParams, **params)

	@staticmethod
	def tearDown():
		"Clean up the network"
		if sys.exc_info != (None, None, None):
			cleanup()

	

	def testPing(self):
		"Create the network and run a ping test"
		net = Mininet(topo=self.topoClass(2, 2, 4, 2), controller=self.controller, host=Host,
			switch=OVSSwitch, link=TCLink, waitConnected=True)
		net.start()
		net.ping()
		# net.ping([net.hosts[0], "10.0.0.2"])
		
	       
		net.myiperf(net.hosts,10)
		

		

		

class TestDatacenter_tier3(testSwitchTopo, unittest.TestCase):
	"Test the HA Root datacenter topolog"
	topoClass= MyTopo
	ryuParams= ['ryu.app.simple_switch_stp']
	mayDrop = 15

if __name__ == '__main__':
	unittest.main()
