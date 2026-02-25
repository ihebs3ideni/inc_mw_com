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

def test_lola_bigdata_exchange(target):
    """Start a sender and receiver for bigdata exchange, wait for receiver to complete."""
    sender_id = target.exec(
        ["/opt/bigdata/bin/bigdata", "--mode", "send", "-t", "40"],
        workdir="/opt/bigdata",
    )
    try:
        recv_id = target.exec(
            ["/opt/bigdata/bin/bigdata", "--mode", "recv", "-n", "25"],
            workdir="/opt/bigdata",
        )
        exit_code = target.wait_exec(recv_id, timeout=30)
        assert exit_code == 0, f"Receiver exited with code {exit_code}"
    finally:
        target.kill_exec(sender_id, signal=15)
