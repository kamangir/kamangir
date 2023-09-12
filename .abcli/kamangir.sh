#! /usr/bin/env bash

function kamangir() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "kamangir update" \
            "update https://github.com/kamangir/kamangir."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m kamangir --help
        fi
        return
    fi

    local function_name=kamangir_$task
    if [[ $(type -t $function_name) == "function" ]] ; then
        $function_name "${@:2}"
        return
    fi

    if [ "$task" == "update" ] ; then
        python3 -m kamangir \
            update \
            "${@:2}"
        return
    fi

    python3 -m kamangir \
        $task \
        ${@:2}
}