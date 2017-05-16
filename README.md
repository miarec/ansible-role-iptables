# ansible-iptables

Ansible role for configuring iptables.

It is based on article [Managing Iptables with Ansible the Easy Way](http://blog.nordeus.com/dev-ops/managing-iptables-with-ansible-the-easy-way.htm).

Role Variables
--------------

- `iptables_keep_unmanaged`: Delete all iptable rules which are not managed by Ansible. Set this to 'yes', if you want the role to keep unmanaged rules. Default is 'no'
- `iptables_default_head`: Default head (allow) rules. By default it allows SSH.
- `iptables_default_tail`: Default tail (deny) rules.

Example Playbook
----------------

eg:

``` yaml
    - name: Configure iptables
      hosts: localhost
      become: yes
      roles:
        - role: ansible-iptables
          iptables_keep_unmanaged: no
          iptables_custom_rules:
            - name: open_web_http
              rules: '-A INPUT -p tcp --dport 80 -j ACCEPT'
              state: present
            - name: open_web_https
              rules: '-A INPUT -p tcp --dport 443 -j ACCEPT'
              state: present
          
```

The above playbook will open TCP 80 and 443 ports and enable iptables.


Default values
--------------

``` yaml
    # defaults/main.yml
    ---
    # Default head (allow) rules
    iptables_default_head: |
      -P INPUT ACCEPT
      -P FORWARD ACCEPT
      -P OUTPUT ACCEPT
      -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
      -A INPUT -i lo -j ACCEPT
      -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
      -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT

    # Default tail (deny) rules
    iptables_default_tail: |
      -A INPUT -j REJECT
      -A FORWARD -j REJECT

    iptables_custom_rules: []
    # Example:
    # iptables_custom_rules:
    #   - name: open_port_12345 # 'iptables_custom_rules_' will be prepended to this
    #     rules: '-A INPUT -p tcp --dport 12345 -j ACCEPT'
    #     state: present
    #     weight: 40
    #     ipversion: 4
    #     table: filter
    #
    # NOTE: 'name', 'rules' and 'state' are required, others are optional.

    # By default this role deletes all iptables rules which are not managed by Ansible.
    # Set this to 'yes', if you want the role to keep unmanaged rules.
    iptables_keep_unmanaged: no
```    


