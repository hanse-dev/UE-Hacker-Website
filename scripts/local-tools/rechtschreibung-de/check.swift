import AppKit
let checker = NSSpellChecker.shared
_ = checker.setLanguage("de")
let data = try! String(contentsOfFile: CommandLine.arguments[1], encoding: .utf8)
for line in data.split(separator: "\n") {
  let parts = line.split(separator: "\t", maxSplits: 1)
  if parts.count < 2 { continue }
  let text = String(parts[1]); let ns = text as NSString
  var pos = 0
  while pos < ns.length {
    let r = checker.checkSpelling(of: text, startingAt: pos, language: "de", wrap: false, inSpellDocumentWithTag: 0, wordCount: nil)
    if r.location == NSNotFound || r.location < pos { break }
    let a = max(0, r.location - 30), b = min(ns.length, r.location + r.length + 30)
    print("\(parts[0])\t\(ns.substring(with: r))\t\(ns.substring(with: NSRange(location: a, length: b - a)))")
    pos = r.location + r.length
  }
}
