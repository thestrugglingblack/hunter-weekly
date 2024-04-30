r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Optional
from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.verify.v2.form import FormList
from twilio.rest.verify.v2.safelist import SafelistList
from twilio.rest.verify.v2.service import ServiceList
from twilio.rest.verify.v2.template import TemplateList
from twilio.rest.verify.v2.verification_attempt import VerificationAttemptList
from twilio.rest.verify.v2.verification_attempts_summary import (
    VerificationAttemptsSummaryList,
)


class V2(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V2 version of Verify

        :param domain: The Twilio.verify domain
        """
        super().__init__(domain, "v2")
        self._forms: Optional[FormList] = None
        self._safelist: Optional[SafelistList] = None
        self._services: Optional[ServiceList] = None
        self._templates: Optional[TemplateList] = None
        self._verification_attempts: Optional[VerificationAttemptList] = None
        self._verification_attempts_summary: Optional[
            VerificationAttemptsSummaryList
        ] = None

    @property
    def forms(self) -> FormList:
        if self._forms is None:
            self._forms = FormList(self)
        return self._forms

    @property
    def safelist(self) -> SafelistList:
        if self._safelist is None:
            self._safelist = SafelistList(self)
        return self._safelist

    @property
    def services(self) -> ServiceList:
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    @property
    def templates(self) -> TemplateList:
        if self._templates is None:
            self._templates = TemplateList(self)
        return self._templates

    @property
    def verification_attempts(self) -> VerificationAttemptList:
        if self._verification_attempts is None:
            self._verification_attempts = VerificationAttemptList(self)
        return self._verification_attempts

    @property
    def verification_attempts_summary(self) -> VerificationAttemptsSummaryList:
        if self._verification_attempts_summary is None:
            self._verification_attempts_summary = VerificationAttemptsSummaryList(self)
        return self._verification_attempts_summary

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2>"
