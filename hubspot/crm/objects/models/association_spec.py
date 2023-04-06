# coding: utf-8

"""
    CRM Objects

    CRM objects such as companies, contacts, deals, line items, products, tickets, and quotes are standard objects in HubSpot’s CRM. These core building blocks support custom properties, store critical information, and play a central role in the HubSpot application.  ## Supported Object Types  This API provides access to collections of CRM objects, which return a map of property names to values. Each object type has its own set of default properties, which can be found by exploring the [CRM Object Properties API](https://developers.hubspot.com/docs/methods/crm-properties/crm-properties-overview).  |Object Type |Properties returned by default | |--|--| | `companies` | `name`, `domain` | | `contacts` | `firstname`, `lastname`, `email` | | `deals` | `dealname`, `amount`, `closedate`, `pipeline`, `dealstage` | | `products` | `name`, `description`, `price` | | `tickets` | `content`, `hs_pipeline`, `hs_pipeline_stage`, `hs_ticket_category`, `hs_ticket_priority`, `subject` |  Find a list of all properties for an object type using the [CRM Object Properties](https://developers.hubspot.com/docs/methods/crm-properties/get-properties) API. e.g. `GET https://api.hubapi.com/properties/v2/companies/properties`. Change the properties returned in the response using the `properties` array in the request body.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.objects.configuration import Configuration


class AssociationSpec(object):
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
    openapi_types = {"association_category": "str", "association_type_id": "int"}

    attribute_map = {"association_category": "associationCategory", "association_type_id": "associationTypeId"}

    def __init__(self, association_category=None, association_type_id=None, local_vars_configuration=None):  # noqa: E501
        """AssociationSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._association_category = None
        self._association_type_id = None
        self.discriminator = None

        self.association_category = association_category
        self.association_type_id = association_type_id

    @property
    def association_category(self):
        """Gets the association_category of this AssociationSpec.  # noqa: E501


        :return: The association_category of this AssociationSpec.  # noqa: E501
        :rtype: str
        """
        return self._association_category

    @association_category.setter
    def association_category(self, association_category):
        """Sets the association_category of this AssociationSpec.


        :param association_category: The association_category of this AssociationSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and association_category is None:  # noqa: E501
            raise ValueError("Invalid value for `association_category`, must not be `None`")  # noqa: E501
        allowed_values = ["HUBSPOT_DEFINED", "USER_DEFINED", "INTEGRATOR_DEFINED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and association_category not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `association_category` ({0}), must be one of {1}".format(association_category, allowed_values))  # noqa: E501

        self._association_category = association_category

    @property
    def association_type_id(self):
        """Gets the association_type_id of this AssociationSpec.  # noqa: E501


        :return: The association_type_id of this AssociationSpec.  # noqa: E501
        :rtype: int
        """
        return self._association_type_id

    @association_type_id.setter
    def association_type_id(self, association_type_id):
        """Sets the association_type_id of this AssociationSpec.


        :param association_type_id: The association_type_id of this AssociationSpec.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and association_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `association_type_id`, must not be `None`")  # noqa: E501

        self._association_type_id = association_type_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
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
        if not isinstance(other, AssociationSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssociationSpec):
            return True

        return self.to_dict() != other.to_dict()
