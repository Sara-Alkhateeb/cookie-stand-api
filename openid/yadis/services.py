# -*- test-case-name: openid.test.test_services -*-

from openid.yadis.filters import mkFilter
from openid.yadis.discover import discover, DiscoveryFailure
from openid.yadis.etxrd import parseXRDS, iterServices, XRDSError


def getServiceEndpoints(input_url, flt=None):
    """Perform the Yadis protocol on the input URL and return an
    iterable of resulting endpoint objects.

    @param flt: A filter object or something that is convertable to
        a filter object (using mkFilter) that will be used to generate
        endpoint objects. This defaults to generating BasicEndpoint
        objects.

    @param input_url: The URL on which to perform the Yadis protocol

    @return: The normalized identity URL and an iterable of endpoint
        objects generated by the filter function.

    @rtype: (str, [endpoint])

    @raises DiscoveryFailure: when Yadis fails to obtain an XRDS document.
    """
    result = discover(input_url)
    try:
        endpoints = applyFilter(result.normalized_uri, result.response_text,
                                flt)
    except XRDSError as err:
        raise DiscoveryFailure(str(err), None)
    return (result.normalized_uri, endpoints)


def applyFilter(normalized_uri, xrd_data, flt=None):
    """Generate an iterable of endpoint objects given this input data,
    presumably from the result of performing the Yadis protocol.

    @param normalized_uri: The input URL, after following redirects,
        as in the Yadis protocol.


    @param xrd_data: The XML text the XRDS file fetched from the
        normalized URI.
    @type xrd_data: str

    """
    flt = mkFilter(flt)
    et = parseXRDS(xrd_data)

    endpoints = []
    for service_element in iterServices(et):
        endpoints.extend(
            flt.getServiceEndpoints(normalized_uri, service_element))

    return endpoints