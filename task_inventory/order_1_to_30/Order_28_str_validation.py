
import re
import socket

"""Order 28: Serval string validation.

Reference to http://regexr.com/

For code f'', this is 3.6.1 grammar
"""


class StrValidation(object):

    ipv6_reg = '\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}' \
               '(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|' \
               '(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)' \
               '(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})' \
               '|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))' \
               '|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}' \
               ':((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))' \
               '|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}' \
               ':((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))' \
               '|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}' \
               ':((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))' \
               '|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)' \
               '(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*'

    @staticmethod
    def validate_email(email_str):
        """
        Support char: 0-9a-zA-Z._
        :param email_str: 
        :return: 
        """
        if email_str and len(email_str) >= 5:
            reg = '^[\w\_\.]+@[\w]+(\.+[\w-]{2,5})+$'
            return re.match(reg, email_str) is not None
        return False

    @staticmethod
    def validate_ipv4(ipv4_str):
        if ipv4_str:
            reg = '^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}$'
            return re.match(reg, ipv4_str) is not None
        return False

    @staticmethod
    def validate_ipv4_with_socket(ipv4_str):
        """
        socket.inet_pton can be used in python 3.x or python 2.7.x not in windows
        :param ipv4_str:
        :return:
        """
        try:
            socket.inet_pton(socket.AF_INET, ipv4_str)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(ipv4_str)
            except socket.error:
                return False
            return ipv4_str.count('.') == 3
        except socket.error:  # not a valid address
            return False

        return True

    @staticmethod
    def validate_ipv4_port(ipv4_str):
        if ipv4_str:
            reg = '^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}' \
                  ':(\d|[1-9]\d|[1-9]\d{2,3}|[1-5]\d{4}|6[0-4]\d{3}|654\d{2}|655[0-2]\d|6553[0-5])$'
            return re.match(reg, ipv4_str) is not None
        return False

    @staticmethod
    def validate_ipv4_netmask(ipv4_str):
        if ipv4_str:
            reg = '^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}' \
                  '/(\d|[1-2]\d|3[0-2])$'
            return re.match(reg, ipv4_str) is not None
        return False

    @staticmethod
    def validate_ipv6(ipv6_str):
        if ipv6_str:
            return re.match(f'^{StrValidation.ipv6_reg}$', ipv6_str) is not None
        return False

    @staticmethod
    def validate_ipv6_with_socket(ipv6_str):
        try:
            socket.inet_pton(socket.AF_INET6, ipv6_str)
            return True
        except AttributeError:  # no inet_pton here, sorry
            return False

    @staticmethod
    def validate_ipv6_netmask(ipv6_str):
        if ipv6_str:
            ipv6_netmask_reg = f'^{StrValidation.ipv6_reg}' \
                               f'/(\d|[1-9]\d|1[0-1]\d|12[0-8])$'
            return re.match(ipv6_netmask_reg, ipv6_str) is not None
        return False

    @staticmethod
    def validate_hostname(hostname_str):
        """

        :param hostname_str: Give hostname str
        :return: Boolean
        """
        ipv4_re = re.compile(r'^(?:(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\Z')
        hostname_re = re.compile(r'[\d\w\.\-\_]+\Z')
        if hostname_re.match(hostname_str) is None:
            return False

        if ipv4_re.match(hostname_str) is not None:
            return True

        hostname_split = hostname_str.split('.')
        if len(hostname_split) <= 4:
            flag_count = 0
            for split_str in hostname_split:
                try:
                    if not split_str or int(split_str) <= 255:
                        flag_count = flag_count + 1
                except ValueError:
                    pass
            if flag_count == len(hostname_split):
                return False
        return True

    @staticmethod
    def test():
        print('***** Email *****')
        email_str = 'a@2.co'
        print(email_str, StrValidation.validate_email(email_str))
        email_str = '2_.-ss@3.c2'
        print(email_str, StrValidation.validate_email(email_str))

        print('***** IPv4 *****')
        ip_str = '0.0.0.0'
        print(ip_str, StrValidation.validate_ipv4(ip_str))
        print(ip_str, StrValidation.validate_ipv4_with_socket(ip_str))
        ip_str = '0.0.0.0:2'
        print(ip_str, StrValidation.validate_ipv4_port(ip_str))
        ip_str = '0.0.0.0/2'
        print(ip_str, StrValidation.validate_ipv4_netmask(ip_str))
        ip_str = '0.0.0.0/32'
        print(ip_str, StrValidation.validate_ipv4_netmask(ip_str))
        ip_str = '1.1.1.1/33'
        print(ip_str, StrValidation.validate_ipv4_netmask(ip_str))

        print('***** IPv6 *****')
        ipv6_star = 'aa::1'
        print(ipv6_star, StrValidation.validate_ipv6(ipv6_star))
        print(ipv6_star, StrValidation.validate_ipv6_with_socket(ipv6_star))
        ipv6_star = 'aa:bb:cc:dd:ee:ff:1:2'
        print(ipv6_star, StrValidation.validate_ipv6(ipv6_star))
        ipv6_star = '2001:0db8:85a3:08d3:1319:8a2e:0370:7334'
        print(ipv6_star, StrValidation.validate_ipv6(ipv6_star))

        ipv6_star = 'aa::1/0'
        print(ipv6_star, StrValidation.validate_ipv6_netmask(ipv6_star))
        ipv6_star = 'aa:bb:cc:dd:ee:ff:1:2/128'
        print(ipv6_star, StrValidation.validate_ipv6_netmask(ipv6_star))
        ipv6_star = '2001:0db8:85a3:08d3:1319:8a2e:0370:7334/129'
        print(ipv6_star, StrValidation.validate_ipv6_netmask(ipv6_star))

    @staticmethod
    def test_validate_hostname():
        hostname = '222aDFaas'
        print(StrValidation.validate_hostname(hostname_str=hostname), hostname)
        hostname = '222.'
        print(StrValidation.validate_hostname(hostname_str=hostname), hostname)
        hostname = '222.2'
        print(StrValidation.validate_hostname(hostname_str=hostname), hostname)
        hostname = '222.2.'
        print(StrValidation.validate_hostname(hostname_str=hostname), hostname)
        hostname = '222.2.2'
        print(StrValidation.validate_hostname(hostname_str=hostname), hostname)
        hostname = '222.2.2.'
        print(StrValidation.validate_hostname(hostname_str=hostname), hostname)
        hostname = '222.2.2.2'
        print(StrValidation.validate_hostname(hostname_str=hostname), hostname)


StrValidation.test_validate_hostname()
