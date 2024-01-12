;;; Utils for building BattMo doc

;; Use user-login-name to get user name
;; (cond '(compare-strings user-login-name "xavier")

(pcase (user-login-name)
  ("xavier" (progn
              (pyvenv-activate "~/Python/battinfodoc.env/")
              (setq docdir "/home/xavier/Python/domain-electrochemistry/sphinx/")
              (setq testdir "/home/xavier/Python/BattInfo-doc-test/")
              ))

  )

(defun battinfodoc-local-open ()
  "Open locally built documentation in browser"
  (interactive)
  (browse-url (concat docdir "_build/html/index.html"))
  )

(defun battinfodoc-build ()
  "Build BattMo documentation"
  (interactive)
  (let* ((default-directory docdir)
         (outputbuffer (get-buffer-create "*buildoutput*"))
         )
    (pop-to-buffer outputbuffer)
    (erase-buffer)
    (start-process "battinfo-build" outputbuffer "make" "html")
    )
  )

(defun battinfodoc-build-examples ()
  "Run python publish script"
  (interactive)
  (let ((outputbuffer (get-buffer-create "*publishoutput*"))
        (directory utilsdir))
    (pop-to-buffer outputbuffer)
    (erase-buffer)
    (start-process "battinfo-publish" outputbuffer "python" (concat directory "buildPublishedExamples.py"))
    )
  )

(defun battinfodoc-publish ()
  "Copy and paste build directory in doc repo and push the result. Then open in a browser the action page in the repo and the published page"
  (interactive)
  (let ((default-directory docdir))
    (shell-command (concat "cp -rf _build/html/* " testdir))
    )
  (let ((default-directory testdir))
    (shell-command "git add *" )
    (shell-command "git commit -m \"update in doc\"")
    (shell-command "git push -f" )
    )
  (browse-url "https://github.com/BattMoTeam/BattInfo-doc-test/actions")
  (browse-url "https://battmoteam.github.io/BattInfo-doc-test/")
  )

