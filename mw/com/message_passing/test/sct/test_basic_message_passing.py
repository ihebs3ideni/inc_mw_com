# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************

COMMANDER_CMD = ["/opt/messaging_app_mqueue/bin/messaging_app_mqueue", "-m", "send", "-n", "10", "-b", "5"]
CONTROLLER_CMD = ["/opt/messaging_app_mqueue/bin/messaging_app_mqueue", "-m", "recv", "-n", "10", "-b", "5"]
WORKDIR = "/opt/messaging_app_mqueue"


def test_basic_message_passing_commander_first(docker_sandbox):
    """
    Start commander (sender) first, then controller (receiver).
    Commander sends a sequence of messages validated by the controller.
    """
    commander_id = docker_sandbox.exec(COMMANDER_CMD, workdir=WORKDIR)
    controller_id = docker_sandbox.exec(CONTROLLER_CMD, workdir=WORKDIR)

    controller_exit = docker_sandbox.wait_exec(controller_id, timeout=30)
    assert controller_exit == 0, f"Controller exited with code {controller_exit}"

    commander_exit = docker_sandbox.wait_exec(commander_id, timeout=30)
    assert commander_exit == 0, f"Commander exited with code {commander_exit}"


def test_basic_message_passing_controller_first(docker_sandbox):
    """
    Start controller (receiver) first, then commander (sender).
    Commander sends a sequence of messages validated by the controller.
    """
    controller_id = docker_sandbox.exec(CONTROLLER_CMD, workdir=WORKDIR)
    commander_id = docker_sandbox.exec(COMMANDER_CMD, workdir=WORKDIR)

    commander_exit = docker_sandbox.wait_exec(commander_id, timeout=30)
    assert commander_exit == 0, f"Commander exited with code {commander_exit}"

    controller_exit = docker_sandbox.wait_exec(controller_id, timeout=30)
    assert controller_exit == 0, f"Controller exited with code {controller_exit}"
