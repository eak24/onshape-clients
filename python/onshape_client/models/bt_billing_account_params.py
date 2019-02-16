# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.93
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTBillingAccountParams(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'address': 'BTAddressInfo',
        'force_create': 'bool',
        'password': 'str',
        'token': 'str',
        'company_plan': 'bool',
        'user_id': 'str',
        'company_id': 'str',
        'plan_id': 'str',
        'seats': 'int',
        'domain_prefix': 'str',
        'payment_type': 'int',
        'trial_period_days': 'int',
        'promonthly_enabled': 'bool',
        'reseller_name': 'str',
        'company_name': 'str'
    }

    attribute_map = {
        'address': 'address',
        'force_create': 'forceCreate',
        'password': 'password',
        'token': 'token',
        'company_plan': 'companyPlan',
        'user_id': 'userId',
        'company_id': 'companyId',
        'plan_id': 'planId',
        'seats': 'seats',
        'domain_prefix': 'domainPrefix',
        'payment_type': 'paymentType',
        'trial_period_days': 'trialPeriodDays',
        'promonthly_enabled': 'promonthlyEnabled',
        'reseller_name': 'resellerName',
        'company_name': 'companyName'
    }

    def __init__(self, address=None, force_create=None, password=None, token=None, company_plan=None, user_id=None, company_id=None, plan_id=None, seats=None, domain_prefix=None, payment_type=None, trial_period_days=None, promonthly_enabled=None, reseller_name=None, company_name=None):  # noqa: E501
        """BTBillingAccountParams - a model defined in OpenAPI"""  # noqa: E501

        self._address = None
        self._force_create = None
        self._password = None
        self._token = None
        self._company_plan = None
        self._user_id = None
        self._company_id = None
        self._plan_id = None
        self._seats = None
        self._domain_prefix = None
        self._payment_type = None
        self._trial_period_days = None
        self._promonthly_enabled = None
        self._reseller_name = None
        self._company_name = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if force_create is not None:
            self.force_create = force_create
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token
        if company_plan is not None:
            self.company_plan = company_plan
        if user_id is not None:
            self.user_id = user_id
        if company_id is not None:
            self.company_id = company_id
        if plan_id is not None:
            self.plan_id = plan_id
        if seats is not None:
            self.seats = seats
        if domain_prefix is not None:
            self.domain_prefix = domain_prefix
        if payment_type is not None:
            self.payment_type = payment_type
        if trial_period_days is not None:
            self.trial_period_days = trial_period_days
        if promonthly_enabled is not None:
            self.promonthly_enabled = promonthly_enabled
        if reseller_name is not None:
            self.reseller_name = reseller_name
        if company_name is not None:
            self.company_name = company_name

    @property
    def address(self):
        """Gets the address of this BTBillingAccountParams.  # noqa: E501


        :return: The address of this BTBillingAccountParams.  # noqa: E501
        :rtype: BTAddressInfo
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BTBillingAccountParams.


        :param address: The address of this BTBillingAccountParams.  # noqa: E501
        :type: BTAddressInfo
        """

        self._address = address

    @property
    def force_create(self):
        """Gets the force_create of this BTBillingAccountParams.  # noqa: E501


        :return: The force_create of this BTBillingAccountParams.  # noqa: E501
        :rtype: bool
        """
        return self._force_create

    @force_create.setter
    def force_create(self, force_create):
        """Sets the force_create of this BTBillingAccountParams.


        :param force_create: The force_create of this BTBillingAccountParams.  # noqa: E501
        :type: bool
        """

        self._force_create = force_create

    @property
    def password(self):
        """Gets the password of this BTBillingAccountParams.  # noqa: E501


        :return: The password of this BTBillingAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this BTBillingAccountParams.


        :param password: The password of this BTBillingAccountParams.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def token(self):
        """Gets the token of this BTBillingAccountParams.  # noqa: E501


        :return: The token of this BTBillingAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this BTBillingAccountParams.


        :param token: The token of this BTBillingAccountParams.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def company_plan(self):
        """Gets the company_plan of this BTBillingAccountParams.  # noqa: E501


        :return: The company_plan of this BTBillingAccountParams.  # noqa: E501
        :rtype: bool
        """
        return self._company_plan

    @company_plan.setter
    def company_plan(self, company_plan):
        """Sets the company_plan of this BTBillingAccountParams.


        :param company_plan: The company_plan of this BTBillingAccountParams.  # noqa: E501
        :type: bool
        """

        self._company_plan = company_plan

    @property
    def user_id(self):
        """Gets the user_id of this BTBillingAccountParams.  # noqa: E501


        :return: The user_id of this BTBillingAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BTBillingAccountParams.


        :param user_id: The user_id of this BTBillingAccountParams.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def company_id(self):
        """Gets the company_id of this BTBillingAccountParams.  # noqa: E501


        :return: The company_id of this BTBillingAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTBillingAccountParams.


        :param company_id: The company_id of this BTBillingAccountParams.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def plan_id(self):
        """Gets the plan_id of this BTBillingAccountParams.  # noqa: E501


        :return: The plan_id of this BTBillingAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this BTBillingAccountParams.


        :param plan_id: The plan_id of this BTBillingAccountParams.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def seats(self):
        """Gets the seats of this BTBillingAccountParams.  # noqa: E501


        :return: The seats of this BTBillingAccountParams.  # noqa: E501
        :rtype: int
        """
        return self._seats

    @seats.setter
    def seats(self, seats):
        """Sets the seats of this BTBillingAccountParams.


        :param seats: The seats of this BTBillingAccountParams.  # noqa: E501
        :type: int
        """

        self._seats = seats

    @property
    def domain_prefix(self):
        """Gets the domain_prefix of this BTBillingAccountParams.  # noqa: E501


        :return: The domain_prefix of this BTBillingAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._domain_prefix

    @domain_prefix.setter
    def domain_prefix(self, domain_prefix):
        """Sets the domain_prefix of this BTBillingAccountParams.


        :param domain_prefix: The domain_prefix of this BTBillingAccountParams.  # noqa: E501
        :type: str
        """

        self._domain_prefix = domain_prefix

    @property
    def payment_type(self):
        """Gets the payment_type of this BTBillingAccountParams.  # noqa: E501


        :return: The payment_type of this BTBillingAccountParams.  # noqa: E501
        :rtype: int
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this BTBillingAccountParams.


        :param payment_type: The payment_type of this BTBillingAccountParams.  # noqa: E501
        :type: int
        """

        self._payment_type = payment_type

    @property
    def trial_period_days(self):
        """Gets the trial_period_days of this BTBillingAccountParams.  # noqa: E501


        :return: The trial_period_days of this BTBillingAccountParams.  # noqa: E501
        :rtype: int
        """
        return self._trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, trial_period_days):
        """Sets the trial_period_days of this BTBillingAccountParams.


        :param trial_period_days: The trial_period_days of this BTBillingAccountParams.  # noqa: E501
        :type: int
        """

        self._trial_period_days = trial_period_days

    @property
    def promonthly_enabled(self):
        """Gets the promonthly_enabled of this BTBillingAccountParams.  # noqa: E501


        :return: The promonthly_enabled of this BTBillingAccountParams.  # noqa: E501
        :rtype: bool
        """
        return self._promonthly_enabled

    @promonthly_enabled.setter
    def promonthly_enabled(self, promonthly_enabled):
        """Sets the promonthly_enabled of this BTBillingAccountParams.


        :param promonthly_enabled: The promonthly_enabled of this BTBillingAccountParams.  # noqa: E501
        :type: bool
        """

        self._promonthly_enabled = promonthly_enabled

    @property
    def reseller_name(self):
        """Gets the reseller_name of this BTBillingAccountParams.  # noqa: E501


        :return: The reseller_name of this BTBillingAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._reseller_name

    @reseller_name.setter
    def reseller_name(self, reseller_name):
        """Sets the reseller_name of this BTBillingAccountParams.


        :param reseller_name: The reseller_name of this BTBillingAccountParams.  # noqa: E501
        :type: str
        """

        self._reseller_name = reseller_name

    @property
    def company_name(self):
        """Gets the company_name of this BTBillingAccountParams.  # noqa: E501


        :return: The company_name of this BTBillingAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this BTBillingAccountParams.


        :param company_name: The company_name of this BTBillingAccountParams.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BTBillingAccountParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other