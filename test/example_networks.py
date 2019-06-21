#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# example_networks.py

import numpy as np

import pyphi
from pyphi import utils
from pyphi.macro import Blackbox, MacroSubsystem
from pyphi.network import Network
from pyphi.subsystem import Subsystem

# TODO pass just the subsystem (contains a reference to the network)

standard = pyphi.examples.basic_network
s = pyphi.examples.basic_subsystem
s_state = pyphi.examples.basic_state()


def s_empty():
    net = standard()
    return Subsystem(net, s_state, ())


def s_single():
    net = standard()
    return Subsystem(net, s_state, (1,))


def subsys_n0n2():
    net = standard()
    return Subsystem(net, s_state, (0, 2))


def subsys_n1n2():
    net = standard()
    return Subsystem(net, s_state, (1, 2))


def s_complete():
    net = standard(cm=None)
    return Subsystem(net, s_state, range(net.size))


def noised():
    tpm = np.array([
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.8],
        [0.7, 0.0, 1.0],
        [1.0, 0.0, 0.0],
        [0.2, 0.8, 0.0],
        [1.0, 1.0, 1.0],
        [1.0, 1.0, 0.3],
        [0.1, 1.0, 0.0]
    ])
    cm = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])
    return Network(tpm, cm=cm)


def s_noised():
    n = noised()
    state = (1, 0, 0)
    return Subsystem(n, state, range(n.size))


def noisy_selfloop_single():
    net = pyphi.examples.basic_noisy_selfloop_network()
    state = (1, 0, 0)
    return Subsystem(net, state, (1,))


s_about_to_be_on = (0, 1, 1)
s_just_turned_on = (1, 0, 0)
s_all_off = (0, 0, 0)


def simple(cm=False):
    """ Simple 'AND' network.

    Diagram:

    |           +~~~~~~~+
    |    +~~~~~~+   A   |<~~~~+
    |    | +~~~>| (AND) +~~~+ |
    |    | |    +~~~~~~~+   | |
    |    | |                | |
    |    v |                v |
    |  +~+~+~~~~+      +~~~~~~+~+
    |  |   B    |<~~~~~+    C   |
    |  | (OFF)  +~~~~~>|  (OFF) |
    |  +~~~~~~~~+      +~~~~~~~~+

    TPM:

    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    |  Previous state ~~> Current state |
    |~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~|
    |      A, B, C     |    A, B, C     |
    |~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~|
    |     {0, 0, 0}    |   {0, 0, 0}    |
    |     {0, 0, 1}    |   {0, 0, 0}    |
    |     {0, 1, 0}    |   {0, 0, 0}    |
    |     {0, 1, 1}    |   {1, 0, 0}    |
    |     {1, 0, 0}    |   {0, 0, 0}    |
    |     {1, 0, 1}    |   {0, 0, 0}    |
    |     {1, 1, 0}    |   {0, 0, 0}    |
    |     {1, 1, 1}    |   {0, 0, 0}    |
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """
    tpm = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0]
    ])
    if cm is False:
        cm = None
    return Network(tpm, cm=cm)


def simple_subsys_all_off():
    net = simple()
    return Subsystem(net, s_all_off, range(net.size))


def simple_subsys_all_a_just_on():
    net = simple()
    a_just_turned_on = (1, 0, 0)
    return Subsystem(net, a_just_turned_on, range(net.size))


def big(cm=None):
    """Return a large network."""
    tpm = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ])
    return Network(tpm, cm=cm)


def big_subsys_all():
    """Return the subsystem associated with ``big``."""
    net = big()
    state = (1,) * 5
    return Subsystem(net, state, range(net.size))


big_subsys_all_complete = big_subsys_all


def big_subsys_0_thru_3():
    """Return a subsystem consisting of the first 4 nodes of ``big``."""
    net = big()
    state = (1,) * 5
    return Subsystem(net, state, range(net.size)[:-1])


def reducible(cm=False):
    tpm = np.zeros([2] * 2 + [2])
    if cm is False:
        cm = np.array([[1, 0],
                       [0, 1]])
    r = Network(tpm, cm=cm)
    state = (0, 0)
    # Return the full subsystem
    return Subsystem(r, state, range(r.size))


def rule30(cm=False):
    tpm = np.array([
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    if cm is False:
        cm = np.array([
            [1, 1, 0, 0, 1],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 1, 1],
            [1, 0, 0, 1, 1]
        ])
    rule30 = Network(tpm, cm=cm)
    all_off = (0, 0, 0, 0, 0)
    return Subsystem(rule30, all_off, range(rule30.size))


def trivial():
    """Single-node network with a self-loop."""
    tpm = np.array([
        [1],
        [1]
    ])
    cm = np.array([[1]])
    net = Network(tpm, cm=cm)
    state = (1, )
    return Subsystem(net, state, range(net.size))


def eight_node(cm=False):
    """Eight-node network."""
    tpm = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 0],
        [1, 1, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 1, 1],
        [1, 1, 0, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 0, 1],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0, 1],
        [0, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ])
    if cm is False:
        cm = np.array([
            [1, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1]
        ])
    return Network(tpm, cm=cm)


def eights():
    net = eight_node()
    state = [0] * 8
    return Subsystem(net, state, range(net.size))


def eights_complete():
    net = eight_node(cm=None)
    state = [0] * 8
    return Subsystem(net, state, range(net.size))


def eight_node_sbs(cm=False):
    tpm = [[1] + ([0] * 255)] * 256
    if cm is False:
        cm = np.array([
            [1, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1]
        ])
    return Network(tpm, cm=cm)


def rule152(cm=False):
    tpm = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]
    ])
    if cm is False:
        cm = np.array(
            [[1, 1, 0, 0, 1],
             [1, 1, 1, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 1, 1, 1],
             [1, 0, 0, 1, 1]]
        )
    return Network(tpm, cm=cm)


def rule152_s():
    net = rule152()
    state = [0] * 5
    return Subsystem(net, state, range(net.size))


def rule152_s_complete():
    net = rule152(cm=None)
    state = [0] * 5
    return Subsystem(net, state, range(net.size))


def macro(cm=False):
    tpm = np.array([
        [0.8281, 0.0819, 0.0819, 0.0081],
        [0.0000, 0.0000, 0.9100, 0.0900],
        [0.0000, 0.9100, 0.0000, 0.0900],
        [0.0000, 0.0000, 0.0000, 1.0000]
    ])
    if cm is False:
        cm = np.array([
            [1, 1],
            [1, 1]
        ])
    return Network(tpm, cm=cm)


def macro_s():
    net = macro()
    state = [0] * 2
    return Subsystem(net, state, range(net.size))


def micro(cm=False):
    tpm = np.array([
        [0.2401, 0.1029, 0.1029, 0.0441, 0.1029, 0.0441, 0.0441, 0.0189,
         0.1029, 0.0441, 0.0441, 0.0189, 0.0441, 0.0189, 0.0189, 0.0081],
        [0.2401, 0.1029, 0.1029, 0.0441, 0.1029, 0.0441, 0.0441, 0.0189,
         0.1029, 0.0441, 0.0441, 0.0189, 0.0441, 0.0189, 0.0189, 0.0081],
        [0.2401, 0.1029, 0.1029, 0.0441, 0.1029, 0.0441, 0.0441, 0.0189,
         0.1029, 0.0441, 0.0441, 0.0189, 0.0441, 0.0189, 0.0189, 0.0081],
        [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.4900, 0.2100, 0.2100, 0.0900],
        [0.2401, 0.1029, 0.1029, 0.0441, 0.1029, 0.0441, 0.0441, 0.0189,
         0.1029, 0.0441, 0.0441, 0.0189, 0.0441, 0.0189, 0.0189, 0.0081],
        [0.2401, 0.1029, 0.1029, 0.0441, 0.1029, 0.0441, 0.0441, 0.0189,
         0.1029, 0.0441, 0.0441, 0.0189, 0.0441, 0.0189, 0.0189, 0.0081],
        [0.2401, 0.1029, 0.1029, 0.0441, 0.1029, 0.0441, 0.0441, 0.0189,
         0.1029, 0.0441, 0.0441, 0.0189, 0.0441, 0.0189, 0.0189, 0.0081],
        [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.4900, 0.2100, 0.2100, 0.0900],
        [0.2401, 0.1029, 0.1029, 0.0441, 0.1029, 0.0441, 0.0441, 0.0189,
         0.1029, 0.0441, 0.0441, 0.0189, 0.0441, 0.0189, 0.0189, 0.0081],
        [0.2401, 0.1029, 0.1029, 0.0441, 0.1029, 0.0441, 0.0441, 0.0189,
         0.1029, 0.0441, 0.0441, 0.0189, 0.0441, 0.0189, 0.0189, 0.0081],
        [0.2401, 0.1029, 0.1029, 0.0441, 0.1029, 0.0441, 0.0441, 0.0189,
         0.1029, 0.0441, 0.0441, 0.0189, 0.0441, 0.0189, 0.0189, 0.0081],
        [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.4900, 0.2100, 0.2100, 0.0900],
        [0.0000, 0.0000, 0.0000, 0.4900, 0.0000, 0.0000, 0.0000, 0.2100,
         0.0000, 0.0000, 0.0000, 0.2100, 0.0000, 0.0000, 0.0000, 0.0900],
        [0.0000, 0.0000, 0.0000, 0.4900, 0.0000, 0.0000, 0.0000, 0.2100,
         0.0000, 0.0000, 0.0000, 0.2100, 0.0000, 0.0000, 0.0000, 0.0900],
        [0.0000, 0.0000, 0.0000, 0.4900, 0.0000, 0.0000, 0.0000, 0.2100,
         0.0000, 0.0000, 0.0000, 0.2100, 0.0000, 0.0000, 0.0000, 0.0900],
        [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 1.0000]
    ])
    if cm is False:
        cm = np.array([
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ])
    return Network(tpm, cm=cm)


def micro_s():
    net = micro()
    state = [1] * 4
    return Subsystem(net, state, range(net.size))


def micro_s_all_off():
    net = micro()
    state = [0] * 4
    return Subsystem(net, state, range(net.size))


# TODO: move to pyphi.examples?
def propagation_delay():
    """The basic PyPhi subsystem with COPY gates on each of the connections in
    the original network, blackboxed over two time steps.
    """
    nodes = 8
    tpm = np.zeros((2 ** nodes, nodes))

    for psi, ps in enumerate(utils.all_states(nodes)):
        cs = [0 for i in range(nodes)]
        if ps[5] == 1 or ps[7] == 1:
            cs[0] = 1
        if ps[0] == 1:
            cs[1] = 1
        if ps[1] ^ ps[6]:
            cs[2] = 1
        if ps[2] == 1:
            cs[3] = 1
            cs[7] = 1
        if ps[3] == 1:
            cs[4] = 1
        if ps[4] == 1:
            cs[5] = 1
            cs[6] = 1
        tpm[psi, :] = cs

    cm = np.array([
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
    ])

    # Current state has the OR gate ON
    cs = (1, 0, 0, 0, 0, 0, 0, 0)

    network = Network(tpm, cm)

    # Elements 1, 3, 5, 6, 7 are the COPY gates
    # 0, 2, and 4 correspond to the original OR, XOR, and COPY
    partition = ((0, 5, 7), (3, 4), (1, 2, 6))
    outputs = (0, 2, 4)
    blackbox = Blackbox(partition, outputs)

    # Over two time steps, the system is functionally the same as the basic
    # system
    time_scale = 2

    return MacroSubsystem(network, cs, network.node_indices,
                          time_scale=time_scale, blackbox=blackbox)
