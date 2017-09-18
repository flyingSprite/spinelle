
import re

"""Order 28: Serval string validation.

Reference to http://regexr.com/
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
    def validate_ipv6_netmask(ipv6_str):
        if ipv6_str:
            ipv6_netmask_reg = f'^{StrValidation.ipv6_reg}' \
                               f'/(\d|[1-9]\d|1[0-1]\d|12[0-8])$'
            return re.match(ipv6_netmask_reg, ipv6_str) is not None
        return False

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


# StrValidation.test()
