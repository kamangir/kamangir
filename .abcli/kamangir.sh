#! /usr/bin/env bash

function kamangir() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        kamangir update "$@"
        return
    fi

    if [ "$task" == "init" ]; then
        abcli_init kamangir "${@:2}"
        return
    fi

    if [[ "|pylint|pytest|test|" == *"|$task|"* ]]; then
        abcli_${task} plugin=kamangir,$2 \
            "${@:3}"
        return
    fi

    if [ "$task" == "update" ]; then
        local options=$2

        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            abcli_show_usage "kamangir update [push]" \
                "update README.md."
            return
        fi

        local do_push=$(abcli_option_int "$options" push 0)

        python3 -m kamangir \
            update \
            "${@:3}"

        if [[ "$do_push" == 1 ]]; then
            abcli_git kamangir push \
                "$(python3 -m kamangir version) update"
        else
            abcli_git kamangir status ~all
        fi

        return
    fi

    python3 -m kamangir "$@"
}

abcli_source_path \
    $abcli_path_git/kamangir/.abcli/tests
