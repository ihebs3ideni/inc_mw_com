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

# See documentation in ITF version of test (platform/aas/test/mw/com/test_shared_memory_storage.py)
def test_lola_shared_memory_storage(docker_sandbox):
    """Start sender and receiver for shared memory storage test."""
    sender_id = docker_sandbox.exec(
        ["/opt/shared_memory_storage/bin/shared_memory_storage", "--mode", "send"],
        workdir="/opt/shared_memory_storage",
    )
    try:
        recv_id = docker_sandbox.exec(
            ["/opt/shared_memory_storage/bin/shared_memory_storage", "--mode", "recv"],
            workdir="/opt/shared_memory_storage",
        )
        exit_code = docker_sandbox.wait_exec(recv_id, timeout=15)
        assert exit_code == 0, f"Receiver exited with code {exit_code}"
    finally:
        if docker_sandbox.is_exec_running(sender_id):
            docker_sandbox.kill_exec(sender_id, signal=15)
