;;; Utils for building BattMo doc

;; Use user-login-name to get user name
;; (cond '(compare-strings user-login-name "xavier")

(pcase (user-login-name)
  ("xavier" (progn
              (pyvenv-activate "~/Python/battinfo-doc-3.12-env/")
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

