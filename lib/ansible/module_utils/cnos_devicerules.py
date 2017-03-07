# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by
# Ansible still belong to the author of the module, and may assign their
# own license to the complete work.
#
# Copyright (C) 2017 Lenovo, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Contains device rule and methods
# Lenovo Networking


def getRuleString(deviceType, variableId):
    retVal = variableId + ":"
    if(deviceType == 'g8272_cnos'):
        if variableId in g8272_cnos:
            retVal = retVal + g8272_cnos[variableId]
        else:
            retVal = "The variable " + variableId + " is not supported"
    elif(deviceType == 'g8296_cnos'):
        if variableId in g8296_cnos:
            retVal = retVal + g8296_cnos[variableId]
        else:
            retVal = "The variable " + variableId + " is not supported"
    elif(deviceType == 'g8332_cnos'):
        if variableId in g8332_cnos:
            retVal = retVal + g8332_cnos[variableId]
        else:
            retVal = "The variable " + variableId + " is not supported"
    else:
        if variableId in default_cnos:
            retVal = retVal + default_cnos[variableId]
        else:
            retVal = "The variable " + variableId + " is not supported"
    return retVal
# EOM

default_cnos = {'vlan_id': 'INTEGER_VALUE:1-3999',
                'vlan_id_range': 'INTEGER_VALUE_RANGE:1-3999',
                'vlan_name': 'TEXT:',
                'vlan_flood': 'TEXT_OPTIONS:ipv4,ipv6',
                'vlan_state': 'TEXT_OPTIONS:active,suspend',
                'vlan_last_member_query_interval': 'INTEGER_VALUE:1-25',
                'vlan_querier': 'IPV4Address:',
                'vlan_querier_timeout': 'INTEGER_VALUE:1-65535',
                'vlan_query_interval': 'INTEGER_VALUE:1-18000',
                'vlan_query_max_response_time': 'INTEGER_VALUE:1-25',
                'vlan_report_suppression': 'INTEGER_VALUE:1-25',
                'vlan_robustness_variable': 'INTEGER_VALUE:1-7',
                'vlan_startup_query_count': 'INTEGER_VALUE:1-10',
                'vlan_startup_query_interval': 'INTEGER_VALUE:1-18000',
                'vlan_snooping_version': 'INTEGER_VALUE:2-3',
                'vlan_access_map_name': 'TEXT: ',
                'vlan_ethernet_interface': 'TEXT:',
                'vlan_portagg_number': 'INTEGER_VALUE:1-4096',
                'vlan_accessmap_action': 'TEXT_OPTIONS:drop,forward,redirect',
                'vlan_dot1q_tag': 'MATCH_TEXT_OR_EMPTY:egress-only',
                'vlan_filter_name': 'TEXT:',
                'vlag_auto_recovery': 'INTEGER_VALUE:240-3600',
                'vlag_config_consistency': 'TEXT_OPTIONS:disable,strict',
                'vlag_instance': 'INTEGER_VALUE:1-64',
                'vlag_port_aggregation': 'INTEGER_VALUE:1-4096',
                'vlag_priority': 'INTEGER_VALUE:0-65535',
                'vlag_startup_delay': 'INTEGER_VALUE:0-3600',
                'vlag_tier_id': 'INTEGER_VALUE:1-512',
                'vlag_hlthchk_options': 'TEXT_OPTIONS:keepalive-attempts,\
                keepalive-interval,peer-ip,retry-interval',
                'vlag_keepalive_attempts': 'INTEGER_VALUE:1-24',
                'vlag_keepalive_interval': 'INTEGER_VALUE:2-300',
                'vlag_retry_interval': 'INTEGER_VALUE:1-300',
                'vlag_peerip': 'IPV4Address:',
                'vlag_peerip_vrf': 'TEXT_OPTIONS:default,management',
                'bgp_as_number': 'NO_VALIDATION:1-4294967295',
                'bgp_address_family': 'TEXT_OPTIONS:ipv4,ipv6',
                'bgp_bgp_local_count': 'INTEGER_VALUE:2-64',
                'cluster_id_as_ip': 'IPV4Address:',
                'cluster_id_as_number': 'NO_VALIDATION:1-4294967295',
                'confederation_identifier': 'INTEGER_VALUE:1-65535',
                'condeferation_peers_as': 'INTEGER_VALUE:1-65535',
                'stalepath_delay_value': 'INTEGER_VALUE:1-3600',
                'maxas_limit_as': 'INTEGER_VALUE:1-2000',
                'neighbor_ipaddress': 'IPV4Address:',
                'neighbor_as': 'NO_VALIDATION:1-4294967295',
                'router_id': 'IPV4Address:',
                'bgp_keepalive_interval': 'INTEGER_VALUE:0-3600',
                'bgp_holdtime': 'INTEGER_VALUE:0-3600',
                'bgp_aggregate_prefix': 'IPV4AddressWithMask:',
                'addrfamily_routemap_name': 'TEXT:',
                'reachability_half_life': 'INTEGER_VALUE:1-45',
                'start_reuse_route_value': 'INTEGER_VALUE:1-20000',
                'start_suppress_route_value': 'INTEGER_VALUE:1-20000',
                'max_duration_to_suppress_route': 'INTEGER_VALUE:1-255',
                'unreachability_halftime_for_penalty': 'INTEGER_VALUE:1-45',
                'distance_external_AS': 'INTEGER_VALUE:1-255',
                'distance_internal_AS': 'INTEGER_VALUE:1-255',
                'distance_local_routes': 'INTEGER_VALUE:1-255',
                'maxpath_option': 'TEXT_OPTIONS:ebgp,ibgp',
                'maxpath_numbers': 'INTEGER_VALUE:2-32',
                'network_ip_prefix_with_mask': 'IPV4AddressWithMask:',
                'network_ip_prefix_value': 'IPV4Address:',
                'network_ip_prefix_mask': 'IPV4Address:',
                'nexthop_crtitical_delay': 'NO_VALIDATION:1-4294967295',
                'nexthop_noncrtitical_delay': 'NO_VALIDATION:1-4294967295',
                'addrfamily_redistribute_option': 'TEXT_OPTIONS:direct,ospf,\
                static',
                'bgp_neighbor_af_occurances': 'INTEGER_VALUE:1-10',
                'bgp_neighbor_af_filtername': 'TEXT:',
                'bgp_neighbor_af_maxprefix': 'INTEGER_VALUE:1-15870',
                'bgp_neighbor_af_prefixname': 'TEXT:',
                'bgp_neighbor_af_routemap': 'TEXT:',
                'bgp_neighbor_address_family': 'TEXT_OPTIONS:ipv4,ipv6',
                'bgp_neighbor_connection_retrytime': 'INTEGER_VALUE:1-65535',
                'bgp_neighbor_description': 'TEXT:',
                'bgp_neighbor_maxhopcount': 'INTEGER_VALUE:1-255',
                'bgp_neighbor_local_as': 'NO_VALIDATION:1-4294967295',
                'bgp_neighbor_maxpeers': 'INTEGER_VALUE:1-96',
                'bgp_neighbor_password': 'TEXT:',
                'bgp_neighbor_timers_Keepalive': 'INTEGER_VALUE:0-3600',
                'bgp_neighbor_timers_holdtime': 'INTEGER_VALUE:0-3600',
                'bgp_neighbor_ttl_hops': 'INTEGER_VALUE:1-254',
                'bgp_neighbor_update_options': 'TEXT_OPTIONS:ethernet,loopback,\
                vlan',
                'bgp_neighbor_update_ethernet': 'TEXT:',
                'bgp_neighbor_update_loopback': 'INTEGER_VALUE:0-7',
                'bgp_neighbor_update_vlan': 'INTEGER_VALUE:1-4094',
                'bgp_neighbor_weight': 'INTEGER_VALUE:0-65535',
                'ethernet_interface_value': 'INTEGER_VALUE:1-54',
                'ethernet_interface_range': 'INTEGER_VALUE_RANGE:1-54',
                'ethernet_interface_string': 'TEXT:',
                'loopback_interface_value': 'INTEGER_VALUE:0-7',
                'mgmt_interface_value': 'INTEGER_VALUE:0-0',
                'vlan_interface_value': 'INTEGER_VALUE:1-4094',
                'portchannel_interface_value': 'INTEGER_VALUE:1-4096',
                'portchannel_interface_range': 'INTEGER_VALUE_RANGE:1-4096',
                'portchannel_interface_string': 'TEXT:',
                'aggregation_group_no': 'INTEGER_VALUE:1-4096',
                'aggregation_group_mode': 'TEXT_OPTIONS:active,on,passive',
                'bfd_options': 'TEXT_OPTIONS:authentication,echo,interval,ipv4,\
                ipv6,neighbor',
                'bfd_interval': 'INTEGER_VALUE:50-999',
                'bfd_minrx': 'INTEGER_VALUE:50-999',
                'bfd_ multiplier': 'INTEGER_VALUE:3-50',
                'bfd_ipv4_options': 'TEXT_OPTIONS:authentication,echo,\
                interval',
                'bfd_auth_options': 'TEXT_OPTIONS:keyed-md5,keyed-sha1,\
                meticulous-keyed-md5,meticulous-keyed-sha1,simple',
                'bfd_key_options': 'TEXT_OPTIONS:key-chain,key-id',
                'bfd_key_chain': 'TEXT:',
                'bfd_key_id': 'INTEGER_VALUE:0-255',
                'bfd_key_name': 'TEXT:',
                'bfd_neighbor_ip': 'TEXT:',
                'bfd_neighbor_options': 'TEXT_OPTIONS:admin-down,multihop,\
                non-persistent',
                'bfd_access_vlan': 'INTEGER_VALUE:1-3999',
                'bfd_bridgeport_mode': 'TEXT_OPTIONS:access,dot1q-tunnel,\
                trunk',
                'trunk_options': 'TEXT_OPTIONS:allowed,native',
                'trunk_vlanid': 'INTEGER_VALUE:1-3999',
                'portCh_description': 'TEXT:',
                'duplex_option': 'TEXT_OPTIONS:auto,full,half',
                'flowcontrol_options': 'TEXT_OPTIONS:receive,send',
                'portchannel_ip_options': 'TEXT_OPTIONS:access-group,address,\
                arp,dhcp,ospf,port,port-unreachable,redirects,router,\
                unreachables',
                'accessgroup_name': 'TEXT:',
                'portchannel_ipv4': 'IPV4Address:',
                'portchannel_ipv4_mask': 'TEXT:',
                'arp_ipaddress': 'IPV4Address:',
                'arp_macaddress': 'TEXT:',
                'arp_timeout_value': 'INTEGER_VALUE:60-28800',
                'relay_ipaddress': 'IPV4Address:',
                'ip_ospf_options': 'TEXT_OPTIONS:authentication,\
                authentication-key,bfd,cost,database-filter,dead-interval,\
                hello-interval,message-digest-key,mtu,mtu-ignore,network,\
                passive-interface,priority,retransmit-interval,shutdown,\
                transmit-delay',
                'ospf_id_decimal_value': 'NO_VALIDATION:1-4294967295',
                'ospf_id_ipaddres_value': 'IPV4Address:',
                'lacp_options': 'TEXT_OPTIONS:port-priority,suspend-individual,\
                timeout',
                'port_priority': 'INTEGER_VALUE:1-65535',
                'lldp_options': 'TEXT_OPTIONS:receive,tlv-select,transmit,\
                trap-notification',
                'lldp_tlv_options': 'TEXT_OPTIONS:link-aggregation,\
                mac-phy-status,management-address,max-frame-size,\
                port-description,port-protocol-vlan,port-vlan,power-mdi,\
                protocol-identity,system-capabilities,system-description,\
                system-name,vid-management,vlan-name',
                'load_interval_delay': 'INTEGER_VALUE:30-300',
                'load_interval_counter': 'INTEGER_VALUE:1-3',
                'mac_accessgroup_name': 'TEXT:',
                'mac_address': 'TEXT:',
                'microburst_threshold': 'NO_VALIDATION:1-4294967295',
                'mtu_value': 'INTEGER_VALUE:64-9216',
                'service_instance': 'NO_VALIDATION:1-4294967295',
                'service_policy_options': 'TEXT_OPTIONS:copp-system-policy,\
                input,output,type',
                'service_policy_name': 'TEXT:',
                'spanning_tree_options': 'TEXT_OPTIONS:bpdufilter,bpduguard,\
                cost,disable,enable,guard,link-type,mst,port,port-priority,\
                vlan',
                'spanning_tree_cost': 'NO_VALIDATION:1-200000000',
                'spanning_tree_interfacerange': 'INTEGER_VALUE_RANGE:1-3999',
                'spanning_tree_portpriority': 'TEXT_OPTIONS:0,32,64,96,128,160,\
                192,224',
                'portchannel_ipv6_neighbor_mac': 'TEXT:',
                'portchannel_ipv6_neighbor_address': 'IPV6Address:',
                'portchannel_ipv6_linklocal': 'IPV6Address:',
                'portchannel_ipv6_dhcp_vlan': 'INTEGER_VALUE:1-4094',
                'portchannel_ipv6_dhcp_ethernet': 'TEXT:',
                'portchannel_ipv6_dhcp': 'IPV6Address:',
                'portchannel_ipv6_address': 'IPV6Address:',
                'portchannel_ipv6_options': 'TEXT_OPTIONS:address,dhcp,\
                link-local,nd,neighbor',
                'interface_speed': 'TEXT_OPTIONS:1000,10000,40000,auto',
                'stormcontrol_options': 'TEXT_OPTIONS:broadcast,multicast,\
                unicast',
                'stormcontrol_level': 'FLOAT:',
                'portchannel_dot1q_tag': 'TEXT_OPTIONS:disable,enable,\
                egress-only',
                'vrrp_id': 'INTEGER_VALUE:1-255',
                }

g8272_cnos = {'vlan_id': 'INTEGER_VALUE:1-3999',
              'vlan_id_range': 'INTEGER_VALUE_RANGE:1-3999',
              'vlan_name': 'TEXT:',
              'vlan_flood': 'TEXT_OPTIONS:ipv4,ipv6',
              'vlan_state': 'TEXT_OPTIONS:active,suspend',
              'vlan_last_member_query_interval': 'INTEGER_VALUE:1-25',
              'vlan_querier': 'IPV4Address:',
              'vlan_querier_timeout': 'INTEGER_VALUE:1-65535',
              'vlan_query_interval': 'INTEGER_VALUE:1-18000',
              'vlan_query_max_response_time': 'INTEGER_VALUE:1-25',
              'vlan_report_suppression': 'INTEGER_VALUE:1-25',
              'vlan_robustness_variable': 'INTEGER_VALUE:1-7',
              'vlan_startup_query_count': 'INTEGER_VALUE:1-10',
              'vlan_startup_query_interval': 'INTEGER_VALUE:1-18000',
              'vlan_snooping_version': 'INTEGER_VALUE:2-3',
              'vlan_access_map_name': 'TEXT: ',
              'vlan_ethernet_interface': 'TEXT:',
              'vlan_portagg_number': 'INTEGER_VALUE:1-4096',
              'vlan_accessmap_action': 'TEXT_OPTIONS:drop,forward,redirect',
              'vlan_dot1q_tag': 'MATCH_TEXT_OR_EMPTY:egress-only',
              'vlan_filter_name': 'TEXT:',
              'vlag_auto_recovery': 'INTEGER_VALUE:240-3600',
              'vlag_config_consistency': 'TEXT_OPTIONS:disable,strict',
              'vlag_instance': 'INTEGER_VALUE:1-64',
              'vlag_port_aggregation': 'INTEGER_VALUE:1-4096',
              'vlag_priority': 'INTEGER_VALUE:0-65535',
              'vlag_startup_delay': 'INTEGER_VALUE:0-3600',
              'vlag_tier_id': 'INTEGER_VALUE:1-512',
              'vlag_hlthchk_options': 'TEXT_OPTIONS:keepalive-attempts,\
              keepalive-interval,peer-ip,retry-interval',
              'vlag_keepalive_attempts': 'INTEGER_VALUE:1-24',
              'vlag_keepalive_interval': 'INTEGER_VALUE:2-300',
              'vlag_retry_interval': 'INTEGER_VALUE:1-300',
              'vlag_peerip': 'IPV4Address:',
              'vlag_peerip_vrf': 'TEXT_OPTIONS:default,management',
              'bgp_as_number': 'NO_VALIDATION:1-4294967295',
              'bgp_address_family': 'TEXT_OPTIONS:ipv4,ipv6',
              'bgp_bgp_local_count': 'INTEGER_VALUE:2-64',
              'cluster_id_as_ip': 'IPV4Address:',
              'cluster_id_as_number': 'NO_VALIDATION:1-4294967295',
              'confederation_identifier': 'INTEGER_VALUE:1-65535',
              'condeferation_peers_as': 'INTEGER_VALUE:1-65535',
              'stalepath_delay_value': 'INTEGER_VALUE:1-3600',
              'maxas_limit_as': 'INTEGER_VALUE:1-2000',
              'neighbor_ipaddress': 'IPV4Address:',
              'neighbor_as': 'NO_VALIDATION:1-4294967295',
              'router_id': 'IPV4Address:',
              'bgp_keepalive_interval': 'INTEGER_VALUE:0-3600',
              'bgp_holdtime': 'INTEGER_VALUE:0-3600',
              'bgp_aggregate_prefix': 'IPV4AddressWithMask:',
              'addrfamily_routemap_name': 'TEXT:',
              'reachability_half_life': 'INTEGER_VALUE:1-45',
              'start_reuse_route_value': 'INTEGER_VALUE:1-20000',
              'start_suppress_route_value': 'INTEGER_VALUE:1-20000',
              'max_duration_to_suppress_route': 'INTEGER_VALUE:1-255',
              'unreachability_halftime_for_penalty': 'INTEGER_VALUE:1-45',
              'distance_external_AS': 'INTEGER_VALUE:1-255',
              'distance_internal_AS': 'INTEGER_VALUE:1-255',
              'distance_local_routes': 'INTEGER_VALUE:1-255',
              'maxpath_option': 'TEXT_OPTIONS:ebgp,ibgp',
              'maxpath_numbers': 'INTEGER_VALUE:2-32',
              'network_ip_prefix_with_mask': 'IPV4AddressWithMask:',
              'network_ip_prefix_value': 'IPV4Address:',
              'network_ip_prefix_mask': 'IPV4Address:',
              'nexthop_crtitical_delay': 'NO_VALIDATION:1-4294967295',
              'nexthop_noncrtitical_delay': 'NO_VALIDATION:1-4294967295',
              'addrfamily_redistribute_option': 'TEXT_OPTIONS:direct,ospf,\
              static',
              'bgp_neighbor_af_occurances': 'INTEGER_VALUE:1-10',
              'bgp_neighbor_af_filtername': 'TEXT:',
              'bgp_neighbor_af_maxprefix': 'INTEGER_VALUE:1-15870',
              'bgp_neighbor_af_prefixname': 'TEXT:',
              'bgp_neighbor_af_routemap': 'TEXT:',
              'bgp_neighbor_address_family': 'TEXT_OPTIONS:ipv4,ipv6',
              'bgp_neighbor_connection_retrytime': 'INTEGER_VALUE:1-65535',
              'bgp_neighbor_description': 'TEXT:',
              'bgp_neighbor_maxhopcount': 'INTEGER_VALUE:1-255',
              'bgp_neighbor_local_as': 'NO_VALIDATION:1-4294967295',
              'bgp_neighbor_maxpeers': 'INTEGER_VALUE:1-96',
              'bgp_neighbor_password': 'TEXT:',
              'bgp_neighbor_timers_Keepalive': 'INTEGER_VALUE:0-3600',
              'bgp_neighbor_timers_holdtime': 'INTEGER_VALUE:0-3600',
              'bgp_neighbor_ttl_hops': 'INTEGER_VALUE:1-254',
              'bgp_neighbor_update_options': 'TEXT_OPTIONS:ethernet,loopback,\
              vlan',
              'bgp_neighbor_update_ethernet': 'TEXT:',
              'bgp_neighbor_update_loopback': 'INTEGER_VALUE:0-7',
              'bgp_neighbor_update_vlan': 'INTEGER_VALUE:1-4094',
              'bgp_neighbor_weight': 'INTEGER_VALUE:0-65535',
              'ethernet_interface_value': 'INTEGER_VALUE:1-54',
              'ethernet_interface_range': 'INTEGER_VALUE_RANGE:1-54',
              'ethernet_interface_string': 'TEXT:',
              'loopback_interface_value': 'INTEGER_VALUE:0-7',
              'mgmt_interface_value': 'INTEGER_VALUE:0-0',
              'vlan_interface_value': 'INTEGER_VALUE:1-4094',
              'portchannel_interface_value': 'INTEGER_VALUE:1-4096',
              'portchannel_interface_range': 'INTEGER_VALUE_RANGE:1-4096',
              'portchannel_interface_string': 'TEXT:',
              'aggregation_group_no': 'INTEGER_VALUE:1-4096',
              'aggregation_group_mode': 'TEXT_OPTIONS:active,on,passive',
              'bfd_options': 'TEXT_OPTIONS:authentication,echo,interval,ipv4,\
              ipv6,neighbor',
              'bfd_interval': 'INTEGER_VALUE:50-999',
              'bfd_minrx': 'INTEGER_VALUE:50-999',
              'bfd_ multiplier': 'INTEGER_VALUE:3-50',
              'bfd_ipv4_options': 'TEXT_OPTIONS:authentication,echo,interval',
              'bfd_auth_options': 'TEXT_OPTIONS:keyed-md5,keyed-sha1,\
              meticulous-keyed-md5,meticulous-keyed-sha1,simple',
              'bfd_key_options': 'TEXT_OPTIONS:key-chain,key-id',
              'bfd_key_chain': 'TEXT:',
              'bfd_key_id': 'INTEGER_VALUE:0-255',
              'bfd_key_name': 'TEXT:',
              'bfd_neighbor_ip': 'TEXT:',
              'bfd_neighbor_options': 'TEXT_OPTIONS:admin-down,multihop,\
              non-persistent',
              'bfd_access_vlan': 'INTEGER_VALUE:1-3999',
              'bfd_bridgeport_mode': 'TEXT_OPTIONS:access,dot1q-tunnel,trunk',
              'trunk_options': 'TEXT_OPTIONS:allowed,native',
              'trunk_vlanid': 'INTEGER_VALUE:1-3999',
              'portCh_description': 'TEXT:',
              'duplex_option': 'TEXT_OPTIONS:auto,full,half',
              'flowcontrol_options': 'TEXT_OPTIONS:receive,send',
              'portchannel_ip_options': 'TEXT_OPTIONS:access-group,address,\
              arp,dhcp,ospf,port,port-unreachable,redirects,router,\
              unreachables',
              'accessgroup_name': 'TEXT:',
              'portchannel_ipv4': 'IPV4Address:',
              'portchannel_ipv4_mask': 'TEXT:',
              'arp_ipaddress': 'IPV4Address:',
              'arp_macaddress': 'TEXT:',
              'arp_timeout_value': 'INTEGER_VALUE:60-28800',
              'relay_ipaddress': 'IPV4Address:',
              'ip_ospf_options': 'TEXT_OPTIONS:authentication,\
              authentication-key,bfd,cost,database-filter,dead-interval,\
              hello-interval,message-digest-key,mtu,mtu-ignore,network,\
              passive-interface,priority,retransmit-interval,shutdown,\
              transmit-delay',
              'ospf_id_decimal_value': 'NO_VALIDATION:1-4294967295',
              'ospf_id_ipaddres_value': 'IPV4Address:',
              'lacp_options': 'TEXT_OPTIONS:port-priority,suspend-individual,\
              timeout',
              'port_priority': 'INTEGER_VALUE:1-65535',
              'lldp_options': 'TEXT_OPTIONS:receive,tlv-select,transmit,\
              trap-notification',
              'lldp_tlv_options': 'TEXT_OPTIONS:link-aggregation,\
              mac-phy-status,management-address,max-frame-size,\
              port-description,port-protocol-vlan,port-vlan,power-mdi,\
              protocol-identity,system-capabilities,system-description,\
              system-name,vid-management,vlan-name',
              'load_interval_delay': 'INTEGER_VALUE:30-300',
              'load_interval_counter': 'INTEGER_VALUE:1-3',
              'mac_accessgroup_name': 'TEXT:',
              'mac_address': 'TEXT:',
              'microburst_threshold': 'NO_VALIDATION:1-4294967295',
              'mtu_value': 'INTEGER_VALUE:64-9216',
              'service_instance': 'NO_VALIDATION:1-4294967295',
              'service_policy_options': 'TEXT_OPTIONS:copp-system-policy,input,\
              output,type',
              'service_policy_name': 'TEXT:',
              'spanning_tree_options': 'TEXT_OPTIONS:bpdufilter,bpduguard,\
              cost,disable,enable,guard,link-type,mst,port,port-priority,vlan',
              'spanning_tree_cost': 'NO_VALIDATION:1-200000000',
              'spanning_tree_interfacerange': 'INTEGER_VALUE_RANGE:1-3999',
              'spanning_tree_portpriority': 'TEXT_OPTIONS:0,32,64,96,128,160,\
              192,224',
              'portchannel_ipv6_neighbor_mac': 'TEXT:',
              'portchannel_ipv6_neighbor_address': 'IPV6Address:',
              'portchannel_ipv6_linklocal': 'IPV6Address:',
              'portchannel_ipv6_dhcp_vlan': 'INTEGER_VALUE:1-4094',
              'portchannel_ipv6_dhcp_ethernet': 'TEXT:',
              'portchannel_ipv6_dhcp': 'IPV6Address:',
              'portchannel_ipv6_address': 'IPV6Address:',
              'portchannel_ipv6_options': 'TEXT_OPTIONS:address,dhcp,\
              link-local,nd,neighbor',
              'interface_speed': 'TEXT_OPTIONS:1000,10000,40000,auto',
              'stormcontrol_options': 'TEXT_OPTIONS:broadcast,multicast,\
              unicast',
              'stormcontrol_level': 'FLOAT:',
              'portchannel_dot1q_tag': 'TEXT_OPTIONS:disable,enable,\
              egress-only',
              'vrrp_id': 'INTEGER_VALUE:1-255',
              }
g8296_cnos = {'vlan_id': 'INTEGER_VALUE:1-3999',
              'vlan_id_range': 'INTEGER_VALUE_RANGE:1-3999',
              'vlan_name': 'TEXT:',
              'vlan_flood': 'TEXT_OPTIONS:ipv4,ipv6',
              'vlan_state': 'TEXT_OPTIONS:active,suspend',
              'vlan_last_member_query_interval': 'INTEGER_VALUE:1-25',
              'vlan_querier': 'IPV4Address:',
              'vlan_querier_timeout': 'INTEGER_VALUE:1-65535',
              'vlan_query_interval': 'INTEGER_VALUE:1-18000',
              'vlan_query_max_response_time': 'INTEGER_VALUE:1-25',
              'vlan_report_suppression': 'INTEGER_VALUE:1-25',
              'vlan_robustness_variable': 'INTEGER_VALUE:1-7',
              'vlan_startup_query_count': 'INTEGER_VALUE:1-10',
              'vlan_startup_query_interval': 'INTEGER_VALUE:1-18000',
              'vlan_snooping_version': 'INTEGER_VALUE:2-3',
              'vlan_access_map_name': 'TEXT: ',
              'vlan_ethernet_interface': 'TEXT:',
              'vlan_portagg_number': 'INTEGER_VALUE:1-4096',
              'vlan_accessmap_action': 'TEXT_OPTIONS:drop,forward,redirect',
              'vlan_dot1q_tag': 'MATCH_TEXT_OR_EMPTY:egress-only',
              'vlan_filter_name': 'TEXT:',
              'vlag_auto_recovery': 'INTEGER_VALUE:240-3600',
              'vlag_config_consistency': 'TEXT_OPTIONS:disable,strict',
              'vlag_instance': 'INTEGER_VALUE:1-128',
              'vlag_port_aggregation': 'INTEGER_VALUE:1-4096',
              'vlag_priority': 'INTEGER_VALUE:0-65535',
              'vlag_startup_delay': 'INTEGER_VALUE:0-3600',
              'vlag_tier_id': 'INTEGER_VALUE:1-512',
              'vlag_hlthchk_options': 'TEXT_OPTIONS:keepalive-attempts,\
              keepalive-interval,peer-ip,retry-interval',
              'vlag_keepalive_attempts': 'INTEGER_VALUE:1-24',
              'vlag_keepalive_interval': 'INTEGER_VALUE:2-300',
              'vlag_retry_interval': 'INTEGER_VALUE:1-300',
              'vlag_peerip': 'IPV4Address:',
              'vlag_peerip_vrf': 'TEXT_OPTIONS:default,management',
              'bgp_as_number': 'NO_VALIDATION:1-4294967295',
              'bgp_address_family': 'TEXT_OPTIONS:ipv4,ipv6',
              'bgp_bgp_local_count': 'INTEGER_VALUE:2-64',
              'cluster_id_as_ip': 'IPV4Address:',
              'cluster_id_as_number': 'NO_VALIDATION:1-4294967295',
              'confederation_identifier': 'INTEGER_VALUE:1-65535',
              'condeferation_peers_as': 'INTEGER_VALUE:1-65535',
              'stalepath_delay_value': 'INTEGER_VALUE:1-3600',
              'maxas_limit_as': 'INTEGER_VALUE:1-2000',
              'neighbor_ipaddress': 'IPV4Address:',
              'neighbor_as': 'NO_VALIDATION:1-4294967295',
              'router_id': 'IPV4Address:',
              'bgp_keepalive_interval': 'INTEGER_VALUE:0-3600',
              'bgp_holdtime': 'INTEGER_VALUE:0-3600',
              'bgp_aggregate_prefix': 'IPV4AddressWithMask:',
              'addrfamily_routemap_name': 'TEXT:',
              'reachability_half_life': 'INTEGER_VALUE:1-45',
              'start_reuse_route_value': 'INTEGER_VALUE:1-20000',
              'start_suppress_route_value': 'INTEGER_VALUE:1-20000',
              'max_duration_to_suppress_route': 'INTEGER_VALUE:1-255',
              'unreachability_halftime_for_penalty': 'INTEGER_VALUE:1-45',
              'distance_external_AS': 'INTEGER_VALUE:1-255',
              'distance_internal_AS': 'INTEGER_VALUE:1-255',
              'distance_local_routes': 'INTEGER_VALUE:1-255',
              'maxpath_option': 'TEXT_OPTIONS:ebgp,ibgp',
              'maxpath_numbers': 'INTEGER_VALUE:2-32',
              'network_ip_prefix_with_mask': 'IPV4AddressWithMask:',
              'network_ip_prefix_value': 'IPV4Address:',
              'network_ip_prefix_mask': 'IPV4Address:',
              'nexthop_crtitical_delay': 'NO_VALIDATION:1-4294967295',
              'nexthop_noncrtitical_delay': 'NO_VALIDATION:1-4294967295',
              'addrfamily_redistribute_option': 'TEXT_OPTIONS:direct,ospf,\
              static',
              'bgp_neighbor_af_occurances': 'INTEGER_VALUE:1-10',
              'bgp_neighbor_af_filtername': 'TEXT:',
              'bgp_neighbor_af_maxprefix': 'INTEGER_VALUE:1-15870',
              'bgp_neighbor_af_prefixname': 'TEXT:',
              'bgp_neighbor_af_routemap': 'TEXT:',
              'bgp_neighbor_address_family': 'TEXT_OPTIONS:ipv4,ipv6',
              'bgp_neighbor_connection_retrytime': 'INTEGER_VALUE:1-65535',
              'bgp_neighbor_description': 'TEXT:',
              'bgp_neighbor_maxhopcount': 'INTEGER_VALUE:1-255',
              'bgp_neighbor_local_as': 'NO_VALIDATION:1-4294967295',
              'bgp_neighbor_maxpeers': 'INTEGER_VALUE:1-96',
              'bgp_neighbor_password': 'TEXT:',
              'bgp_neighbor_timers_Keepalive': 'INTEGER_VALUE:0-3600',
              'bgp_neighbor_timers_holdtime': 'INTEGER_VALUE:0-3600',
              'bgp_neighbor_ttl_hops': 'INTEGER_VALUE:1-254',
              'bgp_neighbor_update_options': 'TEXT_OPTIONS:ethernet,loopback,\
              vlan',
              'bgp_neighbor_update_ethernet': 'TEXT:',
              'bgp_neighbor_update_loopback': 'INTEGER_VALUE:0-7',
              'bgp_neighbor_update_vlan': 'INTEGER_VALUE:1-4094',
              'bgp_neighbor_weight': 'INTEGER_VALUE:0-65535',
              'ethernet_interface_value': 'INTEGER_VALUE:1-96',
              'ethernet_interface_range': 'INTEGER_VALUE_RANGE:1-96',
              'ethernet_interface_string': 'TEXT:',
              'loopback_interface_value': 'INTEGER_VALUE:0-7',
              'mgmt_interface_value': 'INTEGER_VALUE:0-0',
              'vlan_interface_value': 'INTEGER_VALUE:1-4094',
              'portchannel_interface_value': 'INTEGER_VALUE:1-4096',
              'portchannel_interface_range': 'INTEGER_VALUE_RANGE:1-4096',
              'portchannel_interface_string': 'TEXT:',
              'aggregation_group_no': 'INTEGER_VALUE:1-4096',
              'aggregation_group_mode': 'TEXT_OPTIONS:active,on,passive',
              'bfd_options': 'TEXT_OPTIONS:authentication,echo,interval,ipv4,\
              ipv6,neighbor',
              'bfd_interval': 'INTEGER_VALUE:50-999',
              'bfd_minrx': 'INTEGER_VALUE:50-999',
              'bfd_ multiplier': 'INTEGER_VALUE:3-50',
              'bfd_ipv4_options': 'TEXT_OPTIONS:authentication,echo,interval',
              'bfd_auth_options': 'TEXT_OPTIONS:keyed-md5,keyed-sha1,\
              meticulous-keyed-md5,meticulous-keyed-sha1,simple',
              'bfd_key_options': 'TEXT_OPTIONS:key-chain,key-id',
              'bfd_key_chain': 'TEXT:',
              'bfd_key_id': 'INTEGER_VALUE:0-255',
              'bfd_key_name': 'TEXT:',
              'bfd_neighbor_ip': 'TEXT:',
              'bfd_neighbor_options': 'TEXT_OPTIONS:admin-down,multihop,\
              non-persistent',
              'bfd_access_vlan': 'INTEGER_VALUE:1-3999',
              'bfd_bridgeport_mode': 'TEXT_OPTIONS:access,dot1q-tunnel,trunk',
              'trunk_options': 'TEXT_OPTIONS:allowed,native',
              'trunk_vlanid': 'INTEGER_VALUE:1-3999',
              'portCh_description': 'TEXT:',
              'duplex_option': 'TEXT_OPTIONS:auto,full,half',
              'flowcontrol_options': 'TEXT_OPTIONS:receive,send',
              'portchannel_ip_options': 'TEXT_OPTIONS:access-group,address,\
              arp,dhcp,ospf,port,port-unreachable,redirects,router,\
              unreachables',
              'accessgroup_name': 'TEXT:',
              'portchannel_ipv4': 'IPV4Address:',
              'portchannel_ipv4_mask': 'TEXT:',
              'arp_ipaddress': 'IPV4Address:',
              'arp_macaddress': 'TEXT:',
              'arp_timeout_value': 'INTEGER_VALUE:60-28800',
              'relay_ipaddress': 'IPV4Address:',
              'ip_ospf_options': 'TEXT_OPTIONS:authentication,\
              authentication-key,bfd,cost,database-filter,dead-interval,\
              hello-interval,message-digest-key,mtu,mtu-ignore,network,\
              passive-interface,priority,retransmit-interval,shutdown,\
              transmit-delay',
              'ospf_id_decimal_value': 'NO_VALIDATION:1-4294967295',
              'ospf_id_ipaddres_value': 'IPV4Address:',
              'lacp_options': 'TEXT_OPTIONS:port-priority,suspend-individual,\
              timeout',
              'port_priority': 'INTEGER_VALUE:1-65535',
              'lldp_options': 'TEXT_OPTIONS:receive,tlv-select,transmit,\
              trap-notification',
              'lldp_tlv_options': 'TEXT_OPTIONS:link-aggregation,\
              mac-phy-status,management-address,max-frame-size,\
              port-description,port-protocol-vlan,port-vlan,power-mdi,\
              protocol-identity,system-capabilities,system-description,\
              system-name,vid-management,vlan-name',
              'load_interval_delay': 'INTEGER_VALUE:30-300',
              'load_interval_counter': 'INTEGER_VALUE:1-3',
              'mac_accessgroup_name': 'TEXT:',
              'mac_address': 'TEXT:',
              'microburst_threshold': 'NO_VALIDATION:1-4294967295',
              'mtu_value': 'INTEGER_VALUE:64-9216',
              'service_instance': 'NO_VALIDATION:1-4294967295',
              'service_policy_options': 'TEXT_OPTIONS:copp-system-policy,\
              input,output,type',
              'service_policy_name': 'TEXT:',
              'spanning_tree_options': 'TEXT_OPTIONS:bpdufilter,bpduguard,\
              cost,disable,enable,guard,link-type,mst,port,port-priority,vlan',
              'spanning_tree_cost': 'NO_VALIDATION:1-200000000',
              'spanning_tree_interfacerange': 'INTEGER_VALUE_RANGE:1-3999',
              'spanning_tree_portpriority': 'TEXT_OPTIONS:0,32,64,96,128,160,\
              192,224',
              'portchannel_ipv6_neighbor_mac': 'TEXT:',
              'portchannel_ipv6_neighbor_address': 'IPV6Address:',
              'portchannel_ipv6_linklocal': 'IPV6Address:',
              'portchannel_ipv6_dhcp_vlan': 'INTEGER_VALUE:1-4094',
              'portchannel_ipv6_dhcp_ethernet': 'TEXT:',
              'portchannel_ipv6_dhcp': 'IPV6Address:',
              'portchannel_ipv6_address': 'IPV6Address:',
              'portchannel_ipv6_options': 'TEXT_OPTIONS:address,dhcp,\
              link-local,nd,neighbor',
              'interface_speed': 'TEXT_OPTIONS:1000,10000,40000,auto',
              'stormcontrol_options': 'TEXT_OPTIONS:broadcast,multicast,\
              unicast',
              'stormcontrol_level': 'FLOAT:',
              'portchannel_dot1q_tag': 'TEXT_OPTIONS:disable,enable,\
              egress-only',
              'vrrp_id': 'INTEGER_VALUE:1-255',
              }
g8332_cnos = {'vlan_id': 'INTEGER_VALUE:1-3999',
              'vlan_id_range': 'INTEGER_VALUE_RANGE:1-3999',
              'vlan_name': 'TEXT:',
              'vlan_flood': 'TEXT_OPTIONS:ipv4,ipv6',
              'vlan_state': 'TEXT_OPTIONS:active,suspend',
              'vlan_last_member_query_interval': 'INTEGER_VALUE:1-25',
              'vlan_querier': 'IPV4Address:',
              'vlan_querier_timeout': 'INTEGER_VALUE:1-65535',
              'vlan_query_interval': 'INTEGER_VALUE:1-18000',
              'vlan_query_max_response_time': 'INTEGER_VALUE:1-25',
              'vlan_report_suppression': 'INTEGER_VALUE:1-25',
              'vlan_robustness_variable': 'INTEGER_VALUE:1-7',
              'vlan_startup_query_count': 'INTEGER_VALUE:1-10',
              'vlan_startup_query_interval': 'INTEGER_VALUE:1-18000',
              'vlan_snooping_version': 'INTEGER_VALUE:2-3',
              'vlan_access_map_name': 'TEXT: ',
              'vlan_ethernet_interface': 'TEXT:',
              'vlan_portagg_number': 'INTEGER_VALUE:1-4096',
              'vlan_accessmap_action': 'TEXT_OPTIONS:drop,forward,redirect',
              'vlan_dot1q_tag': 'MATCH_TEXT_OR_EMPTY:egress-only',
              'vlan_filter_name': 'TEXT:',
              'vlag_auto_recovery': 'INTEGER_VALUE:240-3600',
              'vlag_config_consistency': 'TEXT_OPTIONS:disable,strict',
              'vlag_instance': 'INTEGER_VALUE:1-128',
              'vlag_port_aggregation': 'INTEGER_VALUE:1-4096',
              'vlag_priority': 'INTEGER_VALUE:0-65535',
              'vlag_startup_delay': 'INTEGER_VALUE:0-3600',
              'vlag_tier_id': 'INTEGER_VALUE:1-512',
              'vlag_hlthchk_options': 'TEXT_OPTIONS:keepalive-attempts,\
              keepalive-interval,peer-ip,retry-interval',
              'vlag_keepalive_attempts': 'INTEGER_VALUE:1-24',
              'vlag_keepalive_interval': 'INTEGER_VALUE:2-300',
              'vlag_retry_interval': 'INTEGER_VALUE:1-300',
              'vlag_peerip': 'IPV4Address:',
              'vlag_peerip_vrf': 'TEXT_OPTIONS:default,management',
              'bgp_as_number': 'NO_VALIDATION:1-4294967295',
              'bgp_address_family': 'TEXT_OPTIONS:ipv4,ipv6',
              'bgp_bgp_local_count': 'INTEGER_VALUE:2-64',
              'cluster_id_as_ip': 'IPV4Address:',
              'cluster_id_as_number': 'NO_VALIDATION:1-4294967295',
              'confederation_identifier': 'INTEGER_VALUE:1-65535',
              'condeferation_peers_as': 'INTEGER_VALUE:1-65535',
              'stalepath_delay_value': 'INTEGER_VALUE:1-3600',
              'maxas_limit_as': 'INTEGER_VALUE:1-2000',
              'neighbor_ipaddress': 'IPV4Address:',
              'neighbor_as': 'NO_VALIDATION:1-4294967295',
              'router_id': 'IPV4Address:',
              'bgp_keepalive_interval': 'INTEGER_VALUE:0-3600',
              'bgp_holdtime': 'INTEGER_VALUE:0-3600',
              'bgp_aggregate_prefix': 'IPV4AddressWithMask:',
              'addrfamily_routemap_name': 'TEXT:',
              'reachability_half_life': 'INTEGER_VALUE:1-45',
              'start_reuse_route_value': 'INTEGER_VALUE:1-20000',
              'start_suppress_route_value': 'INTEGER_VALUE:1-20000',
              'max_duration_to_suppress_route': 'INTEGER_VALUE:1-255',
              'unreachability_halftime_for_penalty': 'INTEGER_VALUE:1-45',
              'distance_external_AS': 'INTEGER_VALUE:1-255',
              'distance_internal_AS': 'INTEGER_VALUE:1-255',
              'distance_local_routes': 'INTEGER_VALUE:1-255',
              'maxpath_option': 'TEXT_OPTIONS:ebgp,ibgp',
              'maxpath_numbers': 'INTEGER_VALUE:2-32',
              'network_ip_prefix_with_mask': 'IPV4AddressWithMask:',
              'network_ip_prefix_value': 'IPV4Address:',
              'network_ip_prefix_mask': 'IPV4Address:',
              'nexthop_crtitical_delay': 'NO_VALIDATION:1-4294967295',
              'nexthop_noncrtitical_delay': 'NO_VALIDATION:1-4294967295',
              'addrfamily_redistribute_option': 'TEXT_OPTIONS:direct,ospf,\
              static',
              'bgp_neighbor_af_occurances': 'INTEGER_VALUE:1-10',
              'bgp_neighbor_af_filtername': 'TEXT:',
              'bgp_neighbor_af_maxprefix': 'INTEGER_VALUE:1-15870',
              'bgp_neighbor_af_prefixname': 'TEXT:',
              'bgp_neighbor_af_routemap': 'TEXT:',
              'bgp_neighbor_address_family': 'TEXT_OPTIONS:ipv4,ipv6',
              'bgp_neighbor_connection_retrytime': 'INTEGER_VALUE:1-65535',
              'bgp_neighbor_description': 'TEXT:',
              'bgp_neighbor_maxhopcount': 'INTEGER_VALUE:1-255',
              'bgp_neighbor_local_as': 'NO_VALIDATION:1-4294967295',
              'bgp_neighbor_maxpeers': 'INTEGER_VALUE:1-96',
              'bgp_neighbor_password': 'TEXT:',
              'bgp_neighbor_timers_Keepalive': 'INTEGER_VALUE:0-3600',
              'bgp_neighbor_timers_holdtime': 'INTEGER_VALUE:0-3600',
              'bgp_neighbor_ttl_hops': 'INTEGER_VALUE:1-254',
              'bgp_neighbor_update_options': 'TEXT_OPTIONS:ethernet,loopback,\
              vlan',
              'bgp_neighbor_update_ethernet': 'TEXT:',
              'bgp_neighbor_update_loopback': 'INTEGER_VALUE:0-7',
              'bgp_neighbor_update_vlan': 'INTEGER_VALUE:1-4094',
              'bgp_neighbor_weight': 'INTEGER_VALUE:0-65535',
              'ethernet_interface_value': 'INTEGER_VALUE:1-32',
              'ethernet_interface_range': 'INTEGER_VALUE_RANGE:1-32',
              'ethernet_interface_string': 'TEXT:',
              'loopback_interface_value': 'INTEGER_VALUE:0-7',
              'mgmt_interface_value': 'INTEGER_VALUE:0-0',
              'vlan_interface_value': 'INTEGER_VALUE:1-4094',
              'portchannel_interface_value': 'INTEGER_VALUE:1-4096',
              'portchannel_interface_range': 'INTEGER_VALUE_RANGE:1-4096',
              'portchannel_interface_string': 'TEXT:',
              'aggregation_group_no': 'INTEGER_VALUE:1-4096',
              'aggregation_group_mode': 'TEXT_OPTIONS:active,on,passive',
              'bfd_options': 'TEXT_OPTIONS:authentication,echo,interval,ipv4,\
              ipv6,neighbor',
              'bfd_interval': 'INTEGER_VALUE:50-999',
              'bfd_minrx': 'INTEGER_VALUE:50-999',
              'bfd_ multiplier': 'INTEGER_VALUE:3-50',
              'bfd_ipv4_options': 'TEXT_OPTIONS:authentication,echo,interval',
              'bfd_auth_options': 'TEXT_OPTIONS:keyed-md5,keyed-sha1,\
              meticulous-keyed-md5,meticulous-keyed-sha1,simple',
              'bfd_key_options': 'TEXT_OPTIONS:key-chain,key-id',
              'bfd_key_chain': 'TEXT:',
              'bfd_key_id': 'INTEGER_VALUE:0-255',
              'bfd_key_name': 'TEXT:',
              'bfd_neighbor_ip': 'TEXT:',
              'bfd_neighbor_options': 'TEXT_OPTIONS:admin-down,multihop,\
              non-persistent',
              'bfd_access_vlan': 'INTEGER_VALUE:1-3999',
              'bfd_bridgeport_mode': 'TEXT_OPTIONS:access,dot1q-tunnel,trunk',
              'trunk_options': 'TEXT_OPTIONS:allowed,native',
              'trunk_vlanid': 'INTEGER_VALUE:1-3999',
              'portCh_description': 'TEXT:',
              'duplex_option': 'TEXT_OPTIONS:auto,full,half',
              'flowcontrol_options': 'TEXT_OPTIONS:receive,send',
              'portchannel_ip_options': 'TEXT_OPTIONS:access-group,address,arp,\
              dhcp,ospf,port,port-unreachable,redirects,router,unreachables',
              'accessgroup_name': 'TEXT:',
              'portchannel_ipv4': 'IPV4Address:',
              'portchannel_ipv4_mask': 'TEXT:',
              'arp_ipaddress': 'IPV4Address:',
              'arp_macaddress': 'TEXT:',
              'arp_timeout_value': 'INTEGER_VALUE:60-28800',
              'relay_ipaddress': 'IPV4Address:',
              'ip_ospf_options': 'TEXT_OPTIONS:authentication,\
              authentication-key,bfd,cost,database-filter,dead-interval,\
              hello-interval,message-digest-key,mtu,mtu-ignore,network,\
              passive-interface,priority,retransmit-interval,shutdown,\
              transmit-delay',
              'ospf_id_decimal_value': 'NO_VALIDATION:1-4294967295',
              'ospf_id_ipaddres_value': 'IPV4Address:',
              'lacp_options': 'TEXT_OPTIONS:port-priority,suspend-individual,\
              timeout',
              'port_priority': 'INTEGER_VALUE:1-65535',
              'lldp_options': 'TEXT_OPTIONS:receive,tlv-select,transmit,\
              trap-notification',
              'lldp_tlv_options': 'TEXT_OPTIONS:link-aggregation,\
              mac-phy-status,management-address,max-frame-size,\
              port-description,port-protocol-vlan,port-vlan,power-mdi,\
              protocol-identity,system-capabilities,system-description,\
              system-name,vid-management,vlan-name',
              'load_interval_delay': 'INTEGER_VALUE:30-300',
              'load_interval_counter': 'INTEGER_VALUE:1-3',
              'mac_accessgroup_name': 'TEXT:',
              'mac_address': 'TEXT:',
              'microburst_threshold': 'NO_VALIDATION:1-4294967295',
              'mtu_value': 'INTEGER_VALUE:64-9216',
              'service_instance': 'NO_VALIDATION:1-4294967295',
              'service_policy_options': 'TEXT_OPTIONS:copp-system-policy,\
              input,output,type',
              'service_policy_name': 'TEXT:',
              'spanning_tree_options': 'TEXT_OPTIONS:bpdufilter,bpduguard,\
              cost,disable,enable,guard,link-type,mst,port,port-priority,vlan',
              'spanning_tree_cost': 'NO_VALIDATION:1-200000000',
              'spanning_tree_interfacerange': 'INTEGER_VALUE_RANGE:1-3999',
              'spanning_tree_portpriority': 'TEXT_OPTIONS:0,32,64,96,128,160,\
              192,224',
              'portchannel_ipv6_neighbor_mac': 'TEXT:',
              'portchannel_ipv6_neighbor_address': 'IPV6Address:',
              'portchannel_ipv6_linklocal': 'IPV6Address:',
              'portchannel_ipv6_dhcp_vlan': 'INTEGER_VALUE:1-4094',
              'portchannel_ipv6_dhcp_ethernet': 'TEXT:',
              'portchannel_ipv6_dhcp': 'IPV6Address:',
              'portchannel_ipv6_address': 'IPV6Address:',
              'portchannel_ipv6_options': 'TEXT_OPTIONS:address,dhcp,\
              link-local,nd,neighbor',
              'interface_speed': 'TEXT_OPTIONS:1000,10000,40000,50000,auto',
              'stormcontrol_options': 'TEXT_OPTIONS:broadcast,multicast,\
              unicast',
              'stormcontrol_level': 'FLOAT:',
              'portchannel_dot1q_tag': 'TEXT_OPTIONS:disable,enable,\
              egress-only',
              'vrrp_id': 'INTEGER_VALUE:1-255',
              }
