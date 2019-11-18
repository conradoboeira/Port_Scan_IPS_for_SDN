"""Custom topology to test tcips

Call it with sudo mn --custom tctopo.py --topo tctopo --controller=remote,ip=127.0.0.1,port=6633 --switch ovs,protocols=OpenFlow13
"""

from mininet.topo import Topo

class TcTopo( Topo ):
    "TC testing topology."

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        host11 = self.addHost( 'h11', ip='10.0.0.11', mac='00:00:00:00:00:11' )
        host12 = self.addHost( 'h12', ip='10.0.0.12', mac='00:00:00:00:00:12' )
        host13 = self.addHost( 'h13', ip='10.0.0.13', mac='00:00:00:00:00:13' )
        host21 = self.addHost( 'h21', ip='10.0.0.21', mac='00:00:00:00:00:21' )
        host31 = self.addHost( 'h31', ip='10.0.0.31', mac='00:00:00:00:00:31' )
        host32 = self.addHost( 'h32', ip='10.0.0.32', mac='00:00:00:00:00:32' )
        host33 = self.addHost( 'h33', ip='10.0.0.33', mac='00:00:00:00:00:33' )
        host41 = self.addHost( 'h41', ip='10.0.0.41', mac='00:00:00:00:00:41' )
        host42 = self.addHost( 'h42', ip='10.0.0.42', mac='00:00:00:00:00:42' ) 
        
        # Add switches
        sw1 = self.addSwitch( 's1' )
        sw2 = self.addSwitch( 's2' )
        sw3 = self.addSwitch( 's3' )
        sw4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( sw1, host11 )#s1-eth1
        self.addLink( sw1, host12 )#s1-eth2
        self.addLink( sw1, host13 )#s1-eth3
        self.addLink( sw1, sw2 )#s1-eth4 - s2-eth1
        self.addLink( sw2, host21 )#s2-eth2
        self.addLink( sw2, sw3 )#s2-eth2 = s3-eth1
        self.addLink( sw3, host31 )#s3-eth2
        self.addLink( sw3, host32 )#s3-eth3
        self.addLink( sw3, host33 )#s3-eth4
        self.addLink( sw2, sw4 )#s2-eth3 s4-eth1
        self.addLink( sw4, host41 )#s4-eth2
        self.addLink( sw4, host42 )#s4-eth3

topos = { 'tctopo': ( lambda: TcTopo() ) }

