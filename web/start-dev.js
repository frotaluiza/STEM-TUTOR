var shell = new ActiveXObject("WScript.Shell");
shell.CurrentDirectory = "C:\\Users\\frota\\Projetos\\ai-stem-tutor\\web";
shell.Run("cmd /c npm run dev", 0, false);
