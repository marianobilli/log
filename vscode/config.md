settings.json
```
{
    "python.pythonPath": ".venv/bin/python3.9",
    "python.linting.pylintEnabled": true,
    "python.linting.enabled": true,
    "editor.quickSuggestions": {
        "other": true,
        "comments": false,
        "strings": false
    },
    "editor.suggestOnTriggerCharacters": true,
    "python.formatting.provider": "autopep8",
    "editor.formatOnSave": true,
    "python.autoComplete.extraPaths": [
        "./other-folder/",
        "./",
    ],
    "code-runner.executorMap": {
        "python": "$pythonPath -u $fullFileName",
    },
    "code-runner.clearPreviousOutput": true,
    "code-runner.showExecutionMessage": false,
    "python.analysis.extraPaths": [
        "./other-folder/",
        "./"
    ]
}
```
