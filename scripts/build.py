#!/usr/bin/env python3
"""Offline chapter audit and Markdown assembler; no external dependencies."""
from pathlib import Path
import argparse,re,sys
p=argparse.ArgumentParser();p.add_argument('--audit',action='store_true');p.add_argument('--preview',action='store_true');p.add_argument('--publication',action='store_true');args=p.parse_args()
root=Path(__file__).resolve().parents[1];folders=sorted((root/'chapters').glob('[0-9][0-9]-*/*'),key=lambda x:int(x.name[:2]));assert len(folders)==36,f'Expected 36 chapter folders, got {len(folders)}'
ready=[];pending=[];bad=[]
for folder in folders:
 file=folder/'chapter.md'
 if not file.exists():pending.append(folder);continue
 content=file.read_text(encoding='utf-8')
 if not content.startswith('---\n') or not re.search(r'^status:\s*approved\s*$',content,re.M):bad.append(folder);continue
 ready.append((folder,content))
print(f'Chapters: {len(folders)} | approved: {len(ready)} | pending: {len(pending)} | unapproved drafts: {len(bad)}')
if args.audit or not(args.preview or args.publication):sys.exit(0)
if args.publication and (pending or bad):sys.exit('Publication blocked: missing or unapproved chapters')
if not ready:sys.exit('No approved chapter.md files to assemble yet')
out=root/'build'/'manuscript.md';out.parent.mkdir(exist_ok=True);out.write_text('# The Data Warrior’s Manuscript\n\n'+'\n\n---\n\n'.join(re.sub(r'^---\n.*?\n---\n','',txt,flags=re.S).strip() for _,txt in ready)+'\n',encoding='utf-8');print('Wrote',out)
