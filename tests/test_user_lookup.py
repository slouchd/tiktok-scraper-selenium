#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest


def test_user_lookup():
    import json
    from src.userlookup import TikTokProfile
    
    lookup = TikTokProfile.get_tiktok_profile("abba", "chrome")
    data = json.loads(lookup)

    username = data.get("username")
    userid = data.get("uid")
    usersecuid = data.get("secuid")

    assert username == "abba"
    assert userid == "6906798265578423298"
    assert usersecuid == "MS4wLjABAAAAPRm9zBYbtJSQidZDPcAaz3dT3D-5qcTBXF7KTaAOOVpYku47tg_S-cEvIRXxplhF"