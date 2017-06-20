# -*- coding: utf-8 -*-

"""
requests.api
~~~~~~~~~~~~

This module allows SSL verifcation to be bypssed in Twisted module

:copyright: (c) 2017 by Vinod Gupta.
:license: Apache2, see LICENSE for more details.
"""

from twisted.web.iweb import IPolicyForHTTPS
from twisted.web.client import _requireSSL
from twisted.internet._sslverify import (_tolerateErrors,
                                         OpenSSLCertificateOptions,
                                         ClientTLSOptions)
from zope.interface import implementer


@implementer(IPolicyForHTTPS)
class CustomPolicyForHTTPS(object):
  """
  SSL connection creator for web clients.
  """
  @_requireSSL
  def creatorForNetloc(self, hostname, port):
    """

    :param hostname:
    :param port:
    :return:
    """
    certificateOptions = OpenSSLCertificateOptions(enableSessions=False)

    client_tls_options = ClientTLSOptions(
      hostname,
      certificateOptions.getContext()
    )

    client_tls_options._ctx.set_info_callback(
      _tolerateErrors(self._identityVerifyingInfoCallback)
    )
    return client_tls_options

  def _identityVerifyingInfoCallback(self, connection, where, ret):
    """

    :param connection:
    :param where:
    :param ret:
    :return:
    """
    pass
    #TODO: implement custom SSL checks as needed here
