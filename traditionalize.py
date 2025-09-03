from opencc import OpenCC
import os

skips = ["node_modules", "public", "cht_replace"]
replaces = {
	"https://github.com/UTCLC/utclc.github.io":"https://github.com/UTCLC/website_cht",
	"utclc.top":"cht.utclc.top",
	r'<ul class="list-inline">你现在正在浏览的是简体中文站。<br>点击前往<a class="font-w-bold" href="https://cht.cht.utclc.top" target="_self">繁体中文站</a>（实验性）。</ul>':
	r'<ul class="list-inline">你現在正在繁體中文站，此站點為實驗性，可能會有潛在的問題。<br>請透過 <a class="font-w-bold" href="https://github.com/UTCLC/website_cht/issues" target="_blank">Github Issue</a> 回報你遇到的錯誤。<br>点击返回<a class="font-w-bold" href="https://utclc.top" target="_self">簡體中文站</a>。</ul>',
	"zh-CN":"zh-TW",
	"zh-hans":"zh-hant",
	"扩展":"拓展",
	"本地化":"在地化",
	"“":"「",
	"”":"」",
	"【":"「",
	"】":"」"
}
replaces_after = {
	"請在此處輸入文字":"請在此處輸入文本",
	"「」":"“”"
}

def readcht(directory):
	directory = "./cht_replace" + directory.removeprefix(".")
	if (not os.path.exists(directory)) or (not os.path.isfile(directory)):
		return ""
	with open(directory, "r", encoding="utf-8") as f:
		return f.read()

def convert(directory):
	for dirfile in os.listdir(directory):
		path = os.path.join(directory, dirfile)
		check = dirfile.startswith(".") or dirfile.endswith(".py") or dirfile in skips
		for skip in skips:
			if (skip in path):
				check = True
		if (check):
			continue
		if (os.path.isdir(path)):
			convert(path)
			continue
		with open(path, "r+", encoding="utf-8") as f:
			print("Converting " + path)
			content = readcht(path)
			if (content == ""):
				try:
					content = f.read()
					for replace in replaces.keys():
						content = content.replace(replace, replaces[replace])
					content = cc.convert(content)
					for replace in replaces_after.keys():
						content = content.replace(replace, replaces_after[replace])
					if (dirfile == "website.md"):
						content = content.replace("cht.utclc.top", "utclc.top")
					f.seek(0)
					f.write(content)
				except:
					print("Error converting " + path)
			else:
				f.write(content)

cc = OpenCC("s2twp.json")
convert(".")