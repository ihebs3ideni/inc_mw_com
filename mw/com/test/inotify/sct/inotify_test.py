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


def test_inotify(target):
    """Run the inotify test binary and wait for it to complete."""
    exec_id = target.exec(
        ["/opt/InotifyTestApp/bin/inotify_test"],
        workdir="/opt/InotifyTestApp",
    )
    exit_code = target.wait_exec(exec_id, timeout=30)
    assert exit_code == 0, f"inotify_test exited with code {exit_code}"
