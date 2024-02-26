import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    s = host.service("iptables")

    assert s.is_enabled
    assert s.is_running

def test_iptables(host):
    assert host.run('iptables --version').rc == 0, "iptables binary should run"


def test_iptables_INPUT(host):

    rules = [
        "-P INPUT ACCEPT",
        "-A INPUT -m state --state RELATED,ESTABLISHED -m comment --comment \"ansible[iptables_default_head]\" -j ACCEPT",
        "-A INPUT -i lo -m comment --comment \"ansible[iptables_default_head]\" -j ACCEPT",
        "-A INPUT -p icmp -m icmp --icmp-type 8 -m comment --comment \"ansible[iptables_default_head]\" -j ACCEPT",
        "-A INPUT -p tcp -m tcp --dport 22 -m comment --comment \"ansible[iptables_default_head]\" -j ACCEPT",
        "-A INPUT -m comment --comment \"ansible[iptables_default_tail]\" -j REJECT --reject-with icmp-port-unreachable"
    ]

    for rule in rules:
        assert rule in host.iptables.rules(), "rule '{}' is not present in INPUT chain".format(rule)

def test_iptables_FORWARD(host):

    rules = [
        "-P FORWARD ACCEPT",
        "-A FORWARD -m comment --comment \"ansible[iptables_default_tail]\" -j REJECT --reject-with icmp-port-unreachable"
    ]

    for rule in rules:
        assert rule in host.iptables.rules(), "rule '{}' is not present in FORWARD chain".format(rule)

