
@@
-    # 1) Apply patches
-    if PATCHES_DIR.exists():
-        for pf in sorted(PATCHES_DIR.rglob("*.md")):
+    # 1) Apply patches (from /Patches and root *_REPLACE files)
+    patch_files = []
+    if PATCHES_DIR.exists():
+        patch_files += sorted(PATCHES_DIR.rglob("*.md"))
+    patch_files += sorted(ROOT.glob("SEC-*_*REPLACE*.md"))
+
+    for pf in patch_files:
             raw = read_text(pf)
             fm, body0 = parse_frontmatter(raw)
             htmlm = parse_html_meta(raw)
             fnm = derive_meta_from_filename(pf)
@@
-            else:
+            else:
                 # No heading; choose whole-file behavior
                 if mode == "append":
                     new_md = tgt_md.rstrip() + "\n\n" + body
                     write_text(tgt, new_md)
                     changes.append(f"APPEND-END: {pf.name} → {tgt.name}")
                 else:
-                    # Whole-file replace only if explicitly flagged
+                    # Whole-file replace only if explicitly flagged
                     if meta.get("target_heading"):
                         # Heading intended but not found. Fallback to APPEND-END to avoid destructive ops.
                         new_md = tgt_md.rstrip() + "\n\n" + body
                         write_text(tgt, new_md)
                         changes.append(f"FALLBACK-APPEND: {pf.name} → {tgt.name} (heading not found)")
                     else:
                         # If file name includes '_REPLACE', allow full replace
                         if "REPLACE" in pf.name.upper():
                             write_text(tgt, body)
                             changes.append(f"FILE-REPLACE: {pf.name} → {tgt.name}")
                         else:
                             new_md = tgt_md.rstrip() + "\n\n" + body
                             write_text(tgt, new_md)
                             changes.append(f"SAFE-APPEND: {pf.name} → {tgt.name}")
