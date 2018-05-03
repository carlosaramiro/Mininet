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

	"""def send_one_file(file_dir, host_pair, files):

		src, dst = host_pair	# a tuple of Mininet node objects

		# choose a random file from files
		rand_fname = random.sample(files, 1)[0]
		rand_path = os.path.join(file_dir, rand_fname)
	
		port = random.randint(1024, 65535)

		# Start listening at the destination host
		dst_cmd = 'nc -1 %d > /home/mininet/sent/%s.out' % (port, rand_frame)
		print os.path.getsize(rand_path)
		dst.popen(dst_cmd, shell=True)

		# Send file from the source host
		src_cmd = 'nc %s %s < %s' % (dst.IP(), port, rand_path)
		src.popen( src_cmd, shell= True )

	def test_netcat_subprocess_async(duration=1, *red):
	
		file_dir = "inputs"
		files = os.listdir(file_dir)

		start_time = time.time()
		end_time = start_time + duration

		# Transfer for the desired duration
		while time.time() < end_time:
			# Choose a pair of hosts
			host_pair = random.sample(red.hosts, 2)

			test_send_one_file_netcat(file_dir, host_pair, files)
	
			interval = random.uniform(0.01, 0.1)
			print "Initialized transfer; waiting %f seconds..." % interval
			time.sleep(interval)"""
	

	def testPing(self):
		"Create the network and run a ping test"
		net = Mininet(topo=self.topoClass(2, 2, 4, 2), controller=self.controller, host=Host,
			switch=OVSSwitch, link=TCLink, waitConnected=True)
		net.start()
		net.ping()
		# net.ping([net.hosts[0], "10.0.0.2"])
		
	        """for i in range (len(net.switches)):
		    net.switches[i].cmdPrint('ovs-vsctl add-port s%s eth1' %i )
	            print "a"
	        for i in range (len(net.hosts)):
		    net.hosts[i].cmdPrint('ifconfig h%s-eth0 0' %i)
		    print "ab"
		    net.hosts[i].cmd('dhclient h%s-eth0' %i)
		    print "b"""
	        CLI(net)
		
		net.switches[4].cmdPrint('ovs-vsctl add-port s4 eth1' )
		print "a"
		"net.hosts[0].cmdPrint('ifconfig h0-eth0 0')"
		print "b"
		net.hosts[0].cmd('dhclient h0-eth0')
		print "ab"

		net.iperf([net.hosts[0], net.hosts[1]])
		net.myiperf(net.hosts,10)
		

		"""try:
			thread.start_new_thread(net.myiperf,(net,net.hosts, 10))
			thread.start_new_thread(net.myiperf,(net,net.hosts, 10))
		except:
			print "Error, unable to start thread"

		while 1:
			pass
		net.stop()"""


		

class TestDatacenter_tier3(testSwitchTopo, unittest.TestCase):
	"Test the HA Root datacenter topolog"
	topoClass= MyTopo
	ryuParams= ['ryu.app.simple_switch_stp']
	mayDrop = 15

if __name__ == '__main__':
	unittest.main()
