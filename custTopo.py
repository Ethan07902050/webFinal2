'''
This file creates simple topology on Mininet for intra and inter domain attacks.
Author: Pranati Kulkarni & Mrinali More
Date: 05/06/2018
CMPE210 course project under Dr.Young Park
'''
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Controller
from mininet.node import RemoteController
from mininet.log import setLogLevel
from mininet.log import info

def createMyTopo():

    net = Mininet(controller=RemoteController)
    info( 'Adding controllers cA and cB\n' )
    cA = net.addController('cA', controller=RemoteController, ip="127.0.0.1", port=6643)
    cB = net.addController('cB', controller=RemoteController, ip="127.0.0.1", port=6634)

    info( 'Adding hosts\n' )
    A1h1 = net.addHost('A1h1', ip='10.0.0.1', mac='0A:01:00:00:00:01')
    A2h2 = net.addHost('A2h2', ip='10.0.0.2', mac='0A:02:00:00:00:02')
    B1h1 = net.addHost('B1h1', ip='10.0.0.3', mac='0B:01:00:00:00:01')
    B2h2 = net.addHost('B2h2', ip='10.0.0.4', mac='0B:02:00:00:00:02')
    C1h1 = net.addHost('C1h1', ip='10.0.0.5', mac='0C:01:00:00:00:01')
    C2h2 = net.addHost('C2h2', ip='10.0.0.6', mac='0C:02:00:00:00:02')
    D1h1 = net.addHost('D1h1', ip='10.0.0.7', mac='0D:01:00:00:00:01')
    D2h2 = net.addHost('D2h2', ip='10.0.0.8', mac='0D:02:00:00:00:02')

    info( 'Adding switches\n' )
    sA = net.addSwitch( 'sA', dpid='0000000000000010' ) 
    s1 = net.addSwitch( 's1', dpid='0000000000000001' )
    s2 = net.addSwitch( 's2', dpid='0000000000000002' )
    sB = net.addSwitch( 'sB', dpid='0000000000000011' )
    s3 = net.addSwitch( 's3', dpid='0000000000000003' )
    s4 = net.addSwitch( 's4', dpid='0000000000000004' )

    net.addLink(A1h1,s1)
    net.addLink(A2h2,s1)
    net.addLink(B1h1,s2)
    net.addLink(B2h2,s2)
    net.addLink(C1h1,s3)
    net.addLink(C2h2,s3)
    net.addLink(D1h1,s4)
    net.addLink(D2h2,s4)
    net.addLink(s1,sA)
    net.addLink(s2,sA)
    net.addLink(s3,sB)
    net.addLink(s4,sB)
    net.addLink(sA,sB)

    info('Building the network\n')
    net.build()
    sA.start([cA])
    s1.start([cA])
    s2.start([cA])
    sB.start([cB])
    s3.start([cB])
    s4.start([cB])

    info('\n Testing pingall\n')
    # net.pingAll()
    CLI(net)
    net.stop()
if __name__ == '__main__':
    setLogLevel( 'info' )
    createMyTopo()
