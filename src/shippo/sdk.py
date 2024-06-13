"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .addresses import Addresses
from .batches import Batches
from .carrier_accounts import CarrierAccounts
from .carrier_parcel_templates import CarrierParcelTemplates
from .customs_declarations import CustomsDeclarations
from .customs_items import CustomsItems
from .manifests import Manifests
from .orders import Orders
from .parcels import Parcels
from .pickups import Pickups
from .rates import Rates
from .rates_at_checkout import RatesAtCheckout
from .refunds import Refunds
from .sdkconfiguration import SDKConfiguration
from .service_groups import ServiceGroups
from .shipments import Shipments
from .shippo_accounts import ShippoAccounts
from .tracking_status import TrackingStatus
from .transactions import Transactions
from .user_parcel_templates import UserParcelTemplates
from .utils.retries import RetryConfig
from .webhooks import Webhooks
from shippo import utils
from shippo._hooks import SDKHooks
from shippo.models import components, internal
from typing import Callable, Dict, Optional, Union

class Shippo:
    r"""Shippo external API.: Use this API to integrate with the Shippo service"""
    addresses: Addresses
    r"""Addresses are the locations a parcel is being shipped **from** and **to**. They represent company and residential places. Among other things, you can use address objects to create shipments, calculate shipping rates, and purchase shipping labels.
    <SchemaDefinition schemaRef=\"#/components/schemas/Address\"/>
    """
    batches: Batches
    r"""A batch is a technique for creating multiple labels at once. Use the  batch object to create and purchase many shipments in two API calls. After creating the batch, retrieve the batch to verify that all shipments are valid. You can add and remove shipments after you have created the batch. When all shipments are valid you can purchase the batch and retrieve all the shipping labels.
    <SchemaDefinition schemaRef=\"#/components/schemas/Batch\"/>

    # Batch Shipment
    The batch shipment object is a wrapper around a shipment object, which include shipment-specific information 
    for batch processing.

    Note: batch shipments can only be created on the batch endpoint, either when creating a batch object or by through 
    the `/batches/{BATCH_OBJECT_ID}/add_shipments` endpoint
    <SchemaDefinition schemaRef=\"#/components/schemas/BatchShipment\"/>
    """
    carrier_accounts: CarrierAccounts
    r"""Carriers are the companies who deliver your package. Shippo uses Carrier account objects as credentials to retrieve shipping rates and purchase labels from shipping Carriers.

    <SchemaDefinition schemaRef=\"#/components/schemas/CarrierAccount\"/>
    """
    customs_declarations: CustomsDeclarations
    r"""Customs declarations are relevant information, including one or multiple customs items, you need to provide for
    customs clearance for your international shipments.
    <SchemaDefinition schemaRef=\"#/components/schemas/CustomsDeclaration\"/>
    """
    customs_items: CustomsItems
    r"""Customs declarations are relevant information, including one or multiple customs items, you need to provide for customs clearance for your international shipments.
    <SchemaDefinition schemaRef=\"#/components/schemas/CustomsItem\"/>
    """
    rates_at_checkout: RatesAtCheckout
    r"""Rates at checkout is a tool for merchants to display up-to-date shipping estimates based on what's in their customers cart and where they’re shipping to.
    Merchants set up curated shipping options for customers in the checkout flow based on data in the shopping cart. The request must include the **to** address and item information. Optional fields are the **from** address and package information. If the optional fields are not included, the service will use the default address and/or package configured for rates at checkout. The response is a list of shipping options based on the Service Group configuration.
    (see <a href=\"#tag/Service-Groups\">Service Group configuration</a> for details).
    <SchemaDefinition schemaRef=\"#/components/schemas/LiveRate\"/>


    # Default Parcel Template
    Assign one of your user parcel templates to be the default used when generating Live Rates. This template will be used by default when generating Live Rates, unless you explicitly provide a parcel in the Live Rates request.
    <SchemaDefinition schemaRef=\"#/components/schemas/UserParcelTemplate\"/>
    """
    manifests: Manifests
    r"""A manifest is a single-page document with a barcode that carriers can scan to accept all packages into transit without the need to scan each item individually.
    They are close-outs of shipping labels of a certain day. Some carriers require manifests to  process the shipments.

    <SchemaDefinition schemaRef=\"#/components/schemas/Manifest\"/>

    # Manifest Errors
    The following codes and messages are the possible errors that may occur when creating Manifests.
    <SchemaDefinition schemaRef=\"#/components/schemas/ManifestErrors\"/>
    """
    orders: Orders
    r"""An order is a request from a customer to purchase goods from a merchant.
    Use the orders object to load orders from your system to the Shippo dashboard.
    You can use the orders object to create, retrieve, list, and manage orders programmatically. 
    You can also retrieve shipping rates, purchase labels, and track shipments for each order.
    <SchemaDefinition schemaRef=\"#/components/schemas/Order\"/>

    # Line Item
    <p style=\"text-align: center; background-color: #F2F3F4;\">
      </br>Line Items, and their corresponding abstract Products and Variants, might be exposed as a separate resource 
      in the future. Currently it's a nested object within the order resource.</br></br>
    </p>
     A line item is an individual object in an order. For example, if your order contains a t-shirt, shorts, and a jacket, each item is represented by a line item.
    <SchemaDefinition schemaRef=\"#/components/schemas/LineItem\"/>
    """
    carrier_parcel_templates: CarrierParcelTemplates
    r"""A carrier parcel template represents a package used for shipping that has preset dimensions defined by a carrier. Some examples of a carrier parcel template include USPS Flat Rate Box and Fedex Small Pak. When using a carrier parcel template, the rates returned may be limited to the carrier that provides the box. You can create user parcel templates using a carrier parcel template. Shippo takes the dimensions of the carrier parcel template but you must configure the weight.

    <SchemaDefinition schemaRef=\"#/components/schemas/CarrierParcelTemplate\"/>
    """
    parcels: Parcels
    r"""A parcel is an item you are shipping. The parcel object includes details about its physical make-up of the parcel. It includes dimensions and weight that Shippo uses to calculate rates.
    <SchemaDefinition schemaRef=\"#/components/schemas/Parcel\"/>

    # Parcel Extras
    The following values are supported for the `extra` field of the parcel object.
    <SchemaDefinition schemaRef=\"#/components/schemas/ParcelExtra\"/>
    """
    pickups: Pickups
    r"""A pickup is when you schedule a carrier to collect a package for delivery.
    Use Shippo’s pickups endpoint to schedule pickups with USPS and DHL Express for eligible shipments that you have already created.
    <SchemaDefinition schemaRef=\"#/components/schemas/Pickup\"/>
    """
    rates: Rates
    r"""A rate is the cost to ship a parcel from a carrier. The rate object details the service level including the cost and transit time.
    <SchemaDefinition schemaRef=\"#/components/schemas/Rate\"/>
    """
    refunds: Refunds
    r"""Refunds are reimbursements for successfully created but unused shipping labels or other charges.
    <SchemaDefinition schemaRef=\"#/components/schemas/Refund\"/>
    """
    service_groups: ServiceGroups
    r"""A service group is a set of service levels grouped together.
    Rates at checkout uses services groups to present available shipping options to customers in their shopping basket.
    <SchemaDefinition schemaRef=\"#/components/schemas/ServiceGroup\"/>
    """
    shipments: Shipments
    r"""A shipment is the act of transporting goods. A shipment object contains **to** and **from** addresses, and the parcel details that you are shipping. You can use the shipment object to retrieve shipping rates and purchase a shipping label.
    <SchemaDefinition schemaRef=\"#/components/schemas/Shipment\"/>

    # Shipment Extras
    The following values are supported for the `extra` field of the shipment object.
    <SchemaDefinition schemaRef=\"#/components/schemas/ShipmentExtra\"/>
    """
    tracking_status: TrackingStatus
    r"""<p style=\\"text-align: center; background-color: #F2F3F4;\\"></br>
    If you purchased your shipping label through Shippo, you can also get all the tracking details of your Shipment 
    from the <a href=\"#tag/Transactions\">Transaction</a> object.
    </br></br></p>
    A tracking status of a package is an indication of current location of a package in the supply chain. For example,  sorting, warehousing, or out for delivery. Use the tracking status object to track the location of your shipments.

    When using your <a href=\"https://docs.goshippo.com/docs/guides_general/authentication/\">Test</a> token for tracking, you need to use Shippo's 
    predefined tokens for testing different tracking statuses. You can find more information in our 
    <a href=\"https://docs.goshippo.com/docs/tracking/tracking/\">Tracking tutorial</a> on how to do this, and what the 
    payloads look like.      
    <SchemaDefinition schemaRef=\"#/components/schemas/Track\"/>
    """
    transactions: Transactions
    r"""A transaction is the purchase of a shipping label from a shipping provider for a specific service. You can print purchased labels and used them to ship a parcel with a carrier, such as USPS or FedEx.
    <SchemaDefinition schemaRef=\"#/components/schemas/Transaction\"/>
    """
    user_parcel_templates: UserParcelTemplates
    r"""A user parcel template represents a package used for shipping that has preset dimensions and attributes defined
    by you. They are useful for capturing attributes of parcel-types you frequently use for shipping, allowing 
    them to be defined once and then used for many shipments. These parcel templates can also be used for live rates.

    User parcel templates can also be created using a carrier parcel template, where the dimensions will be copied from 
    the carrier presets, but the weight can be configured by you.
    <SchemaDefinition schemaRef=\"#/components/schemas/UserParcelTemplate\"/>
    """
    shippo_accounts: ShippoAccounts
    r"""Shippo Accounts are used by Shippo Platform Accounts to create and manage Managed Shippo Accounts.
    Managed Shippo Accounts are headless accounts that represent your customers. They are opaque to your end customers, meaning customers do not need to create their own Shippo login or have a billing relationship with Shippo. 
    They can be used by marketplaces, e-commerce platforms, and third-party logistics providers who want to offer, seamless, built-in shipping functionality to their customers. 
    <SchemaDefinition schemaRef=\"#/components/schemas/ShippoAccount\"/>
    """
    webhooks: Webhooks
    r"""Webhooks are a way for Shippo to notify your application when a specific event occurs. For example, when a label is purchased or when a shipment tracking status has changed. You can use webhooks to trigger actions in your application, such as sending an email or updating a database.
    <SchemaDefinition schemaRef=\"#/components/schemas/Webhook\"/>
    """

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 api_key_header: Union[str, Callable[[], str]],
                 shippo_api_version: str = None,
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param api_key_header: The api_key_header required for authentication
        :type api_key_header: Union[str, Callable[[], str]]
        :param shippo_api_version: Configures the shippo_api_version parameter for all supported operations
        :type shippo_api_version: str
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if callable(api_key_header):
            def security():
                return components.Security(api_key_header = api_key_header())
        else:
            security = components.Security(api_key_header = api_key_header)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    
        _globals = internal.Globals(
            shippo_api_version=shippo_api_version,
        )

        self.sdk_configuration = SDKConfiguration(
            client,
            _globals,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__['_hooks'] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.addresses = Addresses(self.sdk_configuration)
        self.batches = Batches(self.sdk_configuration)
        self.carrier_accounts = CarrierAccounts(self.sdk_configuration)
        self.customs_declarations = CustomsDeclarations(self.sdk_configuration)
        self.customs_items = CustomsItems(self.sdk_configuration)
        self.rates_at_checkout = RatesAtCheckout(self.sdk_configuration)
        self.manifests = Manifests(self.sdk_configuration)
        self.orders = Orders(self.sdk_configuration)
        self.carrier_parcel_templates = CarrierParcelTemplates(self.sdk_configuration)
        self.parcels = Parcels(self.sdk_configuration)
        self.pickups = Pickups(self.sdk_configuration)
        self.rates = Rates(self.sdk_configuration)
        self.refunds = Refunds(self.sdk_configuration)
        self.service_groups = ServiceGroups(self.sdk_configuration)
        self.shipments = Shipments(self.sdk_configuration)
        self.tracking_status = TrackingStatus(self.sdk_configuration)
        self.transactions = Transactions(self.sdk_configuration)
        self.user_parcel_templates = UserParcelTemplates(self.sdk_configuration)
        self.shippo_accounts = ShippoAccounts(self.sdk_configuration)
        self.webhooks = Webhooks(self.sdk_configuration)
