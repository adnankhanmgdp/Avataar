import py_avataaars as pa
import os
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/', methods=["GET", "POST"])
def my_form_post():
    if request.method == "POST":
        myDict = request.form
        naam=str(myDict['naam'])
        if naam=="":
            naam="Default"
        else:
            naam=naam[0].upper()+naam[1:]
        skin_color=str(myDict['skin_color'])
        hair_color=str(myDict['hair_color'])
        facial_hair_type=str(myDict['facial_hair'])
        beard_color=str(myDict['beard_color'])
        top_type=str(myDict['top_type'])
        hat_color=str(myDict['hat_color'])
        mouth_type=str(myDict['mouth_type'])
        eye_type=str(myDict['eye_type'])
        eyebrow_type=str(myDict['eyebrow_type'])
        nose_type=str(myDict['nose_type'])
        accessories_type=str(myDict['accessories_type'])
        clothe_type=str(myDict['clothe_type'])
        clothe_color=str(myDict['clothe_color'])
        if clothe_type!="GRAPHIC_SHIRT":
            clothe_graphic_type="DIAMOND"
        else:
            clothe_graphic_type=str(myDict['clothe_graphic_type'])
        # print(myDict)
        feature=[naam,skin_color,hair_color,facial_hair_type,beard_color,top_type,hat_color,mouth_type,eye_type,eyebrow_type,nose_type,accessories_type,clothe_type,clothe_color,clothe_graphic_type]
        # print(feature)
        avatar = pa.PyAvataaar(
        style=pa.AvatarStyle.CIRCLE,
        # skin_color=pa.SkinColor.DARK_BROWN,
        skin_color=getattr(pa.SkinColor, feature[1]),
        # hair_color=pa.HairColor.BLACK,
        hair_color=getattr(pa.HairColor, feature[2]),
        # facial_hair_type=pa.FacialHairType.DEFAULT,
        facial_hair_type=getattr(pa.FacialHairType, feature[3]),
        # facial_hair_color=pa.FacialHairColor.BLACK,
        facial_hair_color=getattr(pa.FacialHairColor, feature[4]),
        # top_type=pa.TopType.LONG_HAIR_STRAIGHT2,
        top_type=getattr(pa.TopType,feature[5]),
        # hat_color=pa.ClotheColor.BLACK,
        hat_color=getattr(pa.ClotheColor, feature[6]),
        # mouth_type=pa.MouthType.SMILE,
        mouth_type=getattr(pa.MouthType,feature[7]),
        # eye_type=pa.EyesType.DEFAULT,
        eye_type=getattr(pa.EyesType,feature[8]),
        # eyebrow_type=pa.EyebrowType.RAISED_EXCITED,
        eyebrow_type=getattr(pa.EyebrowType,feature[9]),
        # nose_type=pa.NoseType.DEFAULT,
        nose_type=getattr(pa.NoseType,feature[10]),
        # accessories_type=pa.AccessoriesType.DEFAULT,
        accessories_type=getattr(pa.AccessoriesType,feature[11]),
        # clothe_type=pa.ClotheType.GRAPHIC_SHIRT,
        clothe_type=getattr(pa.ClotheType,feature[12]),
        # clothe_color=pa.ClotheColor.RED,
        clothe_color=getattr(pa.ClotheColor,feature[13]),
        # clothe_graphic_type=pa.ClotheGraphicType.DIAMOND,)
        clothe_graphic_type=getattr(pa.ClotheGraphicType,feature[14]),)
        os.chdir('static')
        avatar.render_png_file(f'{feature[0]}.png')
        os.chdir('..')
        full_filename =f'{feature[0]}.png'
        return render_template('show.html', image=full_filename, name=feature[0])
    return render_template('index.html')
if __name__ == "__main__":
    print(os.getcwd())
    app.run(debug=True)