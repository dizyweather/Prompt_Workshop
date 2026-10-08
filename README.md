# Prompt Workshop

A senior thesis interface prototype for helping novice users clarify a prompt before a main model starts working. The demonstration uses the prompt and earlier conversation to offer optional suggestions, then rewrites whole paragraphs as users confirm answers.

## Try the demo

Open `index.html` in a browser. No server, API keys, or installation is needed. Choose the photography website or biology study plan example, then select **Yes, improve it** to enter the workshop or **No, send as is** to skip it.

The initial chat view includes sample projects and two clickable previous chats. The photography and biology chat entries switch between the two staged examples. On narrow screens, use the sidebar button to open the navigation. The numbered **Chat**, **Workshop**, and **Sent** steps also navigate between sections, preserving the draft and version history. Selecting **Sent** sends the current draft into the simulated response view.

The workshop supports direct editing, optional suggestion cards, animated paragraph rewrites, a Completed drawer, and version history with comparison and restoration. A prompt jump and circular ripple reveal the workshop when entering it.

When leaving the workshop, suggestions and history fade away while the prompt moves back into chat and the sidebar returns. **Send current prompt** turns the editor into a submitted message, then reveals the illustrative response after it settles. **Back to chat** returns the prompt to an editable composer draft without sending it. Draft edits remain part of the same version history when reopening the workshop. Reduced motion skips the travel while preserving these outcomes.

Suggestions and responses are scripted for demonstration. Nothing is sent to a model. The communication framework and interception policy remain research decisions; this prototype does not measure output quality or implement a live interceptor.

## Edit and rebuild

- `src/prompt-workshop.html`: editable interface, example content, styles, and interactions; also usable as the inline preview source.
- `index.html`: generated standalone demo.
- `tools/standalone-template.html`: the exported preview shell, including sandbox, theme, and local state support.
- `tools/build_demo.py`: rebuilds the standalone demo with Python's standard library.

After editing the source, run:

```sh
python tools/build_demo.py
python tools/build_demo.py --check
```

Icon and tooltip libraries are loaded from the exported shell's permitted CDNs. The main demo interactions and content do not need a network connection. The browser remembers the latest demo state locally.

## Review checks

Check both staged examples, answering and skipping suggestions, manual edits, version comparison and restoration, sending a draft, and returning to chat. Also check the sidebar at desktop and mobile widths and the transition with reduced motion enabled.
