#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import OVSController
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI

net = Mininet(topo=None, host=CPULimitedHost, link=TCLink, controller=OVSController, build=False)
class FirstTopo( Topo ):
    def __init__ ( self ):
        Topo.__init__( self )
        A = self.addHost( 'A' )
        D = self.addHost( 'D' )
        B = self.addHost( 'B' )
        C = self.addHost( 'C' )
        R1 = self.addSwitch( 'R1' )
        R2 = self.addSwitch( 'R2' )

        self.addLink( A, R1, bw=1000, delay='1ms')
        self.addLink( D, R1, bw=1000, delay='1ms')
        self.addLink( R1, R2, bw=500, delay='10ms')
        self.addLink( B, R2, bw=1000, delay='1ms')
        self.addLink( C, R2, bw=1000, delay='1ms')

def runExperiment():

    topo = FirstTopo()
    net = Mininet (topo)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    runExperiment()

