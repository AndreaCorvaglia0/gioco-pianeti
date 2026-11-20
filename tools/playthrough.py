# Plays the whole story in headless Chromium and saves screenshots in shots/.
# Run from the repository root:  pip install playwright && playwright install chromium && python tools/playthrough.py
# It checks that no page throws an error; it cannot judge touch feel or sound.
import asyncio,os
from playwright.async_api import async_playwright
W,H=844,390
async def main():
    os.makedirs('shots',exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':W,'height':H})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file://'+os.path.abspath('index.html'))
        m=pg.mouse;n=[0]
        async def shot(name):
            n[0]+=1;await pg.screenshot(path=f'shots/{n[0]:02d}_{name}.png')
        async def tap(x,y):
            await m.move(x,y);await m.down();await pg.wait_for_timeout(120);await m.up()
        async def hold(x,y,ms):
            await m.move(x,y);await m.down();await pg.wait_for_timeout(ms);await m.up()
        await pg.wait_for_timeout(800);await tap(342,124);await pg.wait_for_timeout(3500);await shot('mappa1')
        await pg.wait_for_timeout(5000)
        await m.move(200,150);await m.down();await pg.wait_for_timeout(3600);await shot('volo_venere');await pg.wait_for_timeout(9500);await m.up();await pg.wait_for_timeout(1500)
        await hold(180,265,3200);await hold(580,265,4200);await tap(380,117);await pg.wait_for_timeout(4000);await shot('mappa_sole')
        await pg.wait_for_timeout(4500)
        await m.move(200,220);await m.down();await pg.wait_for_timeout(7000);await shot('volo_sole');await pg.wait_for_timeout(6500);await m.up();await pg.wait_for_timeout(2000)
        await shot('sole_arrivo');await pg.wait_for_timeout(2500)
        for x in (300,470,640):
            await tap(x,250);await pg.wait_for_timeout(700)
        await shot('sole_fiammate');await pg.wait_for_timeout(1500);await tap(86,92);await pg.wait_for_timeout(4000);await shot('mappa_fuori')
        await pg.wait_for_timeout(4500)
        await m.move(200,180);await m.down()
        for i in range(4):
            await pg.wait_for_timeout(2600 if i else 3000);await shot(f'volo_saluto{i}')
        await pg.wait_for_timeout(14000);await m.up();await pg.wait_for_timeout(2000);await shot('giove')
        await hold(741,313,2500);await hold(162,363,3000);await pg.wait_for_timeout(3500);await tap(86,92);await pg.wait_for_timeout(9500)
        await m.move(200,200);await m.down();await pg.wait_for_timeout(15000);await m.up();await pg.wait_for_timeout(3000)
        by=lambda x:305-150*(x/W)
        await m.move(100,230);await m.down()
        for i in range(5):
            await m.move(780,190+i*24,steps=40);await m.move(100,200+i*24,steps=40)
        await m.move(764,315,steps=20);await pg.wait_for_timeout(800);await m.up();await pg.wait_for_timeout(4500)
        await shot('mappa_casa');await pg.wait_for_timeout(9500);await shot('fine')
        print('errors',errs);await b.close()
asyncio.run(main())
