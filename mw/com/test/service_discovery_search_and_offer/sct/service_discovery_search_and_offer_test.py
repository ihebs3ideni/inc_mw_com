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

def test_service_discovery_search_and_offer_test(docker_sandbox):
    """Start service, then client. Wait for client to complete."""
    service_id = docker_sandbox.exec(
        ["/opt/ServiceApp/bin/service", "-t", "250"],
        workdir="/opt/ServiceApp",
    )
    try:
        client_id = docker_sandbox.exec(
            ["/opt/ClientApp/bin/client"],
            workdir="/opt/ClientApp",
        )
        exit_code = docker_sandbox.wait_exec(client_id, timeout=30)
        assert exit_code == 0, f"Client exited with code {exit_code}"
    finally:
        docker_sandbox.kill_exec(service_id, signal=15)
