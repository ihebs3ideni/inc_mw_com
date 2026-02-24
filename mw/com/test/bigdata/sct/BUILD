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

load("@rules_oci//oci:defs.bzl", "oci_image", "oci_tarball")
load("@rules_pkg//pkg:tar.bzl", "pkg_tar")
load("@score_itf//:defs.bzl", "py_itf_test")
load("@score_itf//score/itf/plugins:plugins.bzl", "docker")

# Package the stub binary into the path the test expects:
#   /opt/bigdata/bin/bigdata
pkg_tar(
    name = "bigdata-stub-pkg",
    srcs = ["stub/bigdata"],
    package_dir = "opt/bigdata/bin",
    strip_prefix = "stub",
)

oci_image(
    name = "test-image",
    base = "@ubuntu_24_04",
    tars = [":bigdata-stub-pkg"],
)

oci_tarball(
    name = "test-image-tarball",
    image = ":test-image",
    repo_tags = ["mw-com-bigdata-sct:latest"],
)

py_itf_test(
    name = "mw_bigdata_test",
    srcs = ["mw_bigdata_test.py"],
    args = [
        "--docker-image-bootstrap=$(location :test-image-tarball)",
        "--docker-image=mw-com-bigdata-sct:latest",
    ],
    data = [":test-image-tarball"],
    plugins = [docker],
)
