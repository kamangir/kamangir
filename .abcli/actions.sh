#! /usr/bin/env bash

function kamangir_action_git_before_push() {
    kamangir update
    kamangir pypi build
}
