# Benchmark suites from the Fast Downward benchmark collection.

def suite_alternative_formulations():
    return ['airport-adl', 'no-mprime', 'no-mystery']


def suite_ipc98_to_ipc04_adl():
    return [
        'assembly', 'miconic-fulladl', 'miconic-simpleadl',
        'optical-telegraphs', 'philosophers', 'psr-large',
        'psr-middle', 'schedule',
    ]


def suite_ipc98_to_ipc04_strips():
    return [
        'airport', 'blocks', 'depot', 'driverlog', 'freecell', 'grid',
        'gripper', 'logistics00', 'logistics98', 'miconic', 'movie',
        'mprime', 'mystery', 'pipesworld-notankage', 'psr-small',
        'satellite', 'zenotravel',
    ]


def suite_ipc98_to_ipc04():
    # All IPC1-4 domains, including the trivial Movie.
    return sorted(suite_ipc98_to_ipc04_adl() + suite_ipc98_to_ipc04_strips())


def suite_ipc06_adl():
    return [
        'openstacks',
        'pathways',
        'trucks',
    ]


def suite_ipc06_strips_compilations():
    return [
        'openstacks-strips',
        'pathways-noneg',
        'trucks-strips',
    ]


def suite_ipc06_strips():
    return [
        'pipesworld-tankage',
        'rovers',
        'storage',
        'tpp',
    ]


def suite_ipc06():
    return sorted(suite_ipc06_adl() + suite_ipc06_strips())


def suite_ipc08_common_strips():
    return [
        'parcprinter-08-strips',
        'pegsol-08-strips',
        'scanalyzer-08-strips',
    ]


def suite_ipc08_opt_adl():
    return ['openstacks-opt08-adl']


def suite_ipc08_opt_strips():
    return sorted(suite_ipc08_common_strips() + [
        'elevators-opt08-strips',
        'openstacks-opt08-strips',
        'sokoban-opt08-strips',
        'transport-opt08-strips',
        'woodworking-opt08-strips',
    ])


def suite_ipc08_opt():
    return sorted(suite_ipc08_opt_strips() + suite_ipc08_opt_adl())


def suite_ipc08_sat_adl():
    return ['openstacks-sat08-adl']


def suite_ipc08_sat_strips():
    return sorted(suite_ipc08_common_strips() + [
        # Note: cyber-security is missing.
        'elevators-sat08-strips',
        'openstacks-sat08-strips',
        'sokoban-sat08-strips',
        'transport-sat08-strips',
        'woodworking-sat08-strips',
    ])


def suite_ipc08_sat():
    return sorted(suite_ipc08_sat_strips() + suite_ipc08_sat_adl())


def suite_ipc08():
    return sorted(set(suite_ipc08_opt() + suite_ipc08_sat()))


def suite_ipc11_opt():
    return [
        'barman-opt11-strips',
        'elevators-opt11-strips',
        'floortile-opt11-strips',
        'nomystery-opt11-strips',
        'openstacks-opt11-strips',
        'parcprinter-opt11-strips',
        'parking-opt11-strips',
        'pegsol-opt11-strips',
        'scanalyzer-opt11-strips',
        'sokoban-opt11-strips',
        'tidybot-opt11-strips',
        'transport-opt11-strips',
        'visitall-opt11-strips',
        'woodworking-opt11-strips',
    ]


def suite_ipc11_sat():
    return [
        'barman-sat11-strips',
        'elevators-sat11-strips',
        'floortile-sat11-strips',
        'nomystery-sat11-strips',
        'openstacks-sat11-strips',
        'parcprinter-sat11-strips',
        'parking-sat11-strips',
        'pegsol-sat11-strips',
        'scanalyzer-sat11-strips',
        'sokoban-sat11-strips',
        'tidybot-sat11-strips',
        'transport-sat11-strips',
        'visitall-sat11-strips',
        'woodworking-sat11-strips',
    ]


def suite_ipc11():
    return sorted(suite_ipc11_opt() + suite_ipc11_sat())


def suite_ipc14_agl_adl():
    return [
        'cavediving-agl14-adl',
        'citycar-agl14-adl',
        'maintenance-agl14-adl',
    ]


def suite_ipc14_agl_strips():
    return [
        'barman-agl14-strips',
        'childsnack-agl14-strips',
        'floortile-agl14-strips',
        'ged-agl14-strips',
        'hiking-agl14-strips',
        'openstacks-agl14-strips',
        'parking-agl14-strips',
        'tetris-agl14-strips',
        'thoughtful-agl14-strips',
        'transport-agl14-strips',
        'visitall-agl14-strips',
    ]


def suite_ipc14_agl():
    return sorted(suite_ipc14_agl_adl() + suite_ipc14_agl_strips())


def suite_ipc14_mco_adl():
    return [
        'cavediving-mco14-adl',
        'citycar-mco14-adl',
        'maintenance-mco14-adl',
    ]


def suite_ipc14_mco_strips():
    return [
        'barman-mco14-strips',
        'childsnack-mco14-strips',
        'floortile-mco14-strips',
        'ged-mco14-strips',
        'hiking-mco14-strips',
        'openstacks-mco14-strips',
        'parking-mco14-strips',
        'tetris-mco14-strips',
        'thoughtful-mco14-strips',
        'transport-mco14-strips',
        'visitall-mco14-strips',
    ]


def suite_ipc14_mco():
    return sorted(suite_ipc14_mco_adl() + suite_ipc14_mco_strips())


def suite_ipc14_opt_adl():
    return [
        'cavediving-opt14-adl',
        'citycar-opt14-adl',
        'maintenance-opt14-adl',
    ]


def suite_ipc14_opt_strips():
    return [
        'barman-opt14-strips',
        'childsnack-opt14-strips',
        'floortile-opt14-strips',
        'ged-opt14-strips',
        'hiking-opt14-strips',
        'openstacks-opt14-strips',
        'parking-opt14-strips',
        'tetris-opt14-strips',
        'tidybot-opt14-strips',
        'transport-opt14-strips',
        'visitall-opt14-strips',
    ]


def suite_ipc14_opt():
    return sorted(suite_ipc14_opt_adl() + suite_ipc14_opt_strips())


def suite_ipc14_sat_adl():
    return [
        'cavediving-sat14-adl',
        'citycar-sat14-adl',
        'maintenance-sat14-adl',
    ]


def suite_ipc14_sat_strips():
    return [
        'barman-sat14-strips',
        'childsnack-sat14-strips',
        'floortile-sat14-strips',
        'ged-sat14-strips',
        'hiking-sat14-strips',
        'openstacks-sat14-strips',
        'parking-sat14-strips',
        'tetris-sat14-strips',
        'thoughtful-sat14-strips',
        'transport-sat14-strips',
        'visitall-sat14-strips',
    ]


def suite_ipc14_sat():
    return sorted(suite_ipc14_sat_adl() + suite_ipc14_sat_strips())


def suite_ipc14():
    return sorted(
        suite_ipc14_agl() + suite_ipc14_mco() +
        suite_ipc14_opt() + suite_ipc14_sat())


def suite_unsolvable():
    # TODO: Add other unsolvable problems (Miconic-FullADL).
    # TODO: Add 'fsc-grid-r:prize5x5_R.pddl' and 't0-uts:uts_r-02.pddl'
    #       if the extra-domains branch is merged.
    return sorted(
        ['mystery:prob%02d.pddl' % index
         for index in [4, 5, 7, 8, 12, 16, 18, 21, 22, 23, 24]] +
        ['miconic-fulladl:f21-3.pddl', 'miconic-fulladl:f30-2.pddl'])


def suite_optimal_adl():
    return sorted(
        suite_ipc98_to_ipc04_adl() + suite_ipc06_adl() +
        suite_ipc08_opt_adl())


def suite_optimal_strips():
    return sorted(
        suite_ipc98_to_ipc04_strips() + suite_ipc06_strips() +
        suite_ipc06_strips_compilations() + suite_ipc08_opt_strips() +
        suite_ipc11_opt())


def suite_optimal():
    return sorted(suite_optimal_adl() + suite_optimal_strips())


def suite_satisficing_adl():
    return sorted(
        suite_ipc98_to_ipc04_adl() + suite_ipc06_adl() +
        suite_ipc08_sat_adl())


def suite_satisficing_strips():
    return sorted(
        suite_ipc98_to_ipc04_strips() + suite_ipc06_strips() +
        suite_ipc06_strips_compilations() + suite_ipc08_sat_strips() +
        suite_ipc11_sat())


def suite_satisficing():
    return sorted(suite_satisficing_adl() + suite_satisficing_strips())


def suite_all():
    return sorted(
        suite_ipc98_to_ipc04() + suite_ipc06() +
        suite_ipc06_strips_compilations() + suite_ipc08() +
        suite_ipc11() + suite_alternative_formulations())
