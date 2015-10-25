from flask import g

import util
from . import MemberHelper
from db import Kanmusu

def port():
    admiral = g.admiral
    response = {}
    # TODO: Log entry
    response['api_log'] = [{
        "api_state": "0", "api_no": 0, "api_type": "1", "api_message": "ayy lmao"
    }]
    # Background music?
    response["api_p_bgm_id"] = 100
    # This sets the parallel quest count. Don't know what higher values do, default is 5.
    # I set it to ten because fuck the police
    response["api_parallel_quest_count"] = 10
    # Combined flag? Event data probably.
    response["api_combined_flag"] = 0
    # API basic - a replica of api_get_member/basic
    response['api_basic'] = util.merge_two_dicts(MemberHelper.basic(), {
        'api_medals': 0, 'api_large_dock': 0
    })
    # Fleets.
    response['api_deck_port'] = [MemberHelper.fleet(fleet) for fleet in admiral.fleets]
    # Materials.
    response['api_material'] = MemberHelper.material()

    response['api_ship'] = [MemberHelper.kanmusu(kanmusu) for kanmusu in admiral.kanmusu if kanmusu.active]

    # Generate ndock.
    response['api_ndock'] = MemberHelper.rdock()
    return response


def powerup(kanmusu_id, result):
    fleet_data = [MemberHelper.fleet(fleet) for fleet in g.admiral.fleets]
    api_ship = MemberHelper.kanmusu(Kanmusu.get(kanmusu_id))
    return {
        "api_powerup_flag": int(result),
        "api_ship": api_ship,
        "api_deck": fleet_data
    }
