import wikipedia
wikipedia.set_lang('ja')
exts = ['png', 'jpg', 'gif', 'svg', 'tiff']

def ext(path):
  return path.split('.')[-1].lower()

def search(word):
  cands = wikipedia.search(word)
  hit = word in cands
  title = cands[0]
  page =  wikipedia.page(title)
  summary = wikipedia.summary(title)
  imgs = [img for img in page.images if ext(img) in exts]
  rst = {}
  rst['hit'] = hit
  rst['imgs'] = imgs
  rst['summary'] = summary
  rst['title'] = title
  return rst

def test():
  ts = ['チョコレート', 'ふぁが', 'いちご', 'HTML', '金銭感覚']
  for t in ts:
    print('Q:', t)
    print(search(t))

# test()
