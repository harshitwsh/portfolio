def fix_all_text_helpers_clean():
    target_files = [
        'public/assets/main-B9-HtP-f.js',
        'main-B9-HtP-f.js'
    ]

    all_helpers = '''function createShardTextTexture(e,t){let n=document.createElement("canvas");n.width=2048,n.height=1024;let r=n.getContext("2d");r.clearRect(0,0,n.width,n.height),r.fillStyle="#ffffff",r.shadowColor="rgba(0,0,0,0.65)",r.shadowBlur=16,r.shadowOffsetY=4;let i=e.length<=8?210:160;r.font=`700 ${i}px "STK Bureau Serif", "Times New Roman", Georgia, serif`,r.textAlign="center",r.textBaseline="alphabetic",r.fillText(e,1024,460),r.font='400 72px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.fillText(t,1024,620);let a=new dc(n);return a.colorSpace=W,a.generateMipmaps=!0,a.minFilter=v,a.magFilter=v,a.needsUpdate=!0,a};
function createStage3TextTexture(e,t,n=""){let r=document.createElement("canvas");r.width=2400,r.height=1300;let i=r.getContext("2d");i.clearRect(0,0,r.width,r.height);let a=i.createLinearGradient(0,200,0,950);if(a.addColorStop(0,"#ffffff"),a.addColorStop(.3,"#e2faf2"),a.addColorStop(.7,"#c1efe0"),a.addColorStop(1,"#a5e2cf"),i.fillStyle=a,i.shadowColor="rgba(10,35,25,0.5)",i.shadowBlur=20,i.shadowOffsetY=6,n){i.font='400 120px "STK Bureau Serif", "Times New Roman", Georgia, serif',i.textAlign="left",i.textBaseline="alphabetic",i.fillText(e,450,420),i.font='italic 400 240px "Bethany Elingston", "Times New Roman", cursive, serif',i.fillText(t,450,680),i.font='700 160px "STK Bureau Serif", "Times New Roman", Georgia, serif',i.fillText(n,450,880)}else{i.font='400 170px "STK Bureau Serif", "Times New Roman", Georgia, serif',i.textAlign="left",i.textBaseline="alphabetic",i.fillText(e,450,520),i.font='italic 400 290px "Bethany Elingston", "Times New Roman", cursive, serif',i.fillText(t,550,790)}let o=new dc(r);return o.colorSpace=W,o.generateMipmaps=!0,o.minFilter=v,o.magFilter=v,o.needsUpdate=!0,o};
function createEditorialTextTexture(e="Have an Idea.",t="You"){let n=document.createElement("canvas");n.width=2400,n.height=1200;let r=n.getContext("2d");r.clearRect(0,0,n.width,n.height);let i=r.createLinearGradient(0,300,0,850);i.addColorStop(0,"#6c9b8e"),i.addColorStop(.25,"#527e72"),i.addColorStop(.65,"#385b51"),i.addColorStop(1,"#233e36"),r.fillStyle=i,r.shadowColor="rgba(18,42,35,0.32)",r.shadowBlur=18,r.shadowOffsetY=5;let a=e[0],o=e.slice(1);r.font='italic 400 240px "STK Bureau Serif", "Times New Roman", Georgia, serif';let s=r.measureText(a).width;r.font='400 210px "STK Bureau Serif", "Times New Roman", Georgia, serif';let c=r.measureText(o).width,l=s+c,u=(n.width-l)/2,d=720;r.font='400 105px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.textAlign="left",r.textBaseline="alphabetic",r.fillText(t,u+s+15,d-160),r.font='italic 400 240px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.fillText(a,u,d),r.font='400 210px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.fillText(o,u+s-10,d);let f=new dc(n);return f.colorSpace=W,f.generateMipmaps=!0,f.minFilter=v,f.magFilter=v,f.needsUpdate=!0,f};'''

    for filepath in target_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        pos_start = code.find('function createShardTextTexture(')
        if pos_start == -1:
            pos_start = code.find('function createEditorialTextTexture(')
        pos_end = code.find(';var Sb=`/`', pos_start)

        if pos_start != -1 and pos_end != -1:
            code = code[:pos_start] + all_helpers + code[pos_end+1:]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Cleanly updated all text helpers in', filepath)

if __name__ == '__main__':
    fix_all_text_helpers_clean()
