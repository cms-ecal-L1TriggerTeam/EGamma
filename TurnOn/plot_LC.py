import ROOT

logAxis=0

ROOT.gStyle.SetOptTitle(0)

EG_List = ['EB', 'EE']

outfile= ROOT.TFile.Open("output_LC.root","RECREATE")
canvas = ROOT.TCanvas("c", "c", 600, 600)
canvas.Draw()
canvas.SetGridx(1)
canvas.SetGridy(1)
canvas.SetLogx(logAxis)
canvas.SetLeftMargin(0.2)
canvas.SetTopMargin(0.05)
canvas.SetBottomMargin(0.15)
leg = ROOT.TLegend(0.46, 0.6, 0.89, 0.45)

#leg.AddEntry(None, "Z #rightArrow e^{+}e^{-}", "")
#leg.AddEntry(None, "ECAL Barrel", "") 
histList=[]
filein = ROOT.TFile.Open("ratioScan/selectPairsDir/turnons/EG20/LC_eff_EG20_tagWP80_probeWP80_EB_M_vs_EB_M_fitres.root", "READ")
print filein.GetName()
c= filein.Get("ca")
print c.GetName()
outfile.cd()
plist = c.GetListOfPrimitives()
for pl in  plist: print pl.GetName()
histo=c.FindObject("h_data_Eff[l1_20_EB_M]").Clone()
histo.SetName("h_data_Eff_l1_20_EB_M" )
curve=c.FindObject("cb_Norm[sc_et_EB_M]").Clone()
curve.SetName("cb_Norm_sc_et_20_M_EB")
histo2=c.FindObject("h_data2_Eff[l1_20_EB_M]" ).Clone()
histo2.SetName("h_data2_Eff_l1_20_EB_M" )
curve2=c.FindObject("cb2_Norm[sc_et_EB_M]").Clone()
curve2.SetName("cb2_Norm_sc_et_20_M_EB")
curve2.Write()
curve.Write()
histo.Write()
histo2.Write()
canvas.cd()
canvas.SetLogx(logAxis)
histo.Draw("AP")
histo.GetYaxis().SetTitle("Efficiency")
histo.GetXaxis().SetTitle("E_{T} [GeV]")
histo.GetXaxis().SetTitleOffset(1.2)
histo.GetYaxis().SetTitleOffset(1.1)
for point in range(0, histo.GetN()):
    histo.SetPointEXlow(point, 0)
    histo.SetPointEXhigh(point, 0)
        

if logAxis==0:
    histo.GetHistogram().GetXaxis().SetRangeUser(10., 50.) 
    canvas.Update()
else:
    histo.GetHistogram().GetXaxis().SetRangeUser(5.,150.)

canvas.Update()
curve.Draw("SAME")
curve.SetLineColor(1)
histo2.Draw("SAMEP")
histo2.GetYaxis().SetTitle("Efficiency")
histo2.GetXaxis().SetTitle("E_{T} [GeV]")
histo2.GetXaxis().SetTitleOffset(1.2)
histo2.GetYaxis().SetTitleOffset(1.2)
for point in range(0, histo2.GetN()):
    histo2.SetPointEXlow(point, 0)
    histo2.SetPointEXhigh(point, 0)

curve2.Draw("SAME")
curve2.SetLineColor(2)
print histo.GetName()

histo.Draw("SAMEP")
curve.Draw("SAME")
curve.SetLineColor(1)
histo2.Draw("SAMEP")
curve2.Draw("SAME")
curve2.SetLineColor(2)
histo.SetLineColor(1)
histo.SetMarkerStyle(20)
histo.SetMarkerColor(1)
histo2.SetLineColor(2)
histo2.SetMarkerStyle(20)
histo2.SetMarkerColor(2)
leg.SetTextSize(0.034)
leg.AddEntry(None, "BARREL", "")
leg.AddEntry(histo, "New Laser Corrections" , "lp")
leg.AddEntry(histo2, "Old Laser Corrections" , "lp")

label1  = ROOT.TLatex(10., 1.01, "CMS")
label3  = ROOT.TLatex(10., 0.965,  "Preliminary") 
#label1.SetTextFont(42) 
label1.SetTextSize(0.04)
label1.Draw()
label3.SetTextFont(52) 
label3.SetTextSize(0.03)
label3.Draw()

label2  = ROOT.TLatex(80, 1.11, "#sqrt{s}=8 TeV") 
label2.SetTextFont(42) 
label2.SetTextSize(0.04)
label2.Draw()

text = ROOT.TPaveText(0.5, 0.7, 0.88, 0.62,"NBNDC")
text.SetFillColor(0)
text.AddText("Z #rightarrow e^{+}e^{-}")
#text = ROOT.TLatex(30, 0.70, "Z #rightarrow e^{+}e^{-}")
#text.SetTextFont(42) 
text.SetTextSize(0.035)
text.SetTextAlign(11)
text.AddText("L1 Threshold: 20 GeV ")
text.Draw()
#text2 = ROOT.TPaveText(0.5, 0.7, 0.85, 0.65)#ROOT.TLatex(30, 0.65, "L1 Threshold: 20 GeV ")
##text2.SetTextFont(42) 
#text2.SetTextSize(0.035)
#text2.Draw()

filein2 = ROOT.TFile.Open("ratioScan/selectPairsDir/turnons/EG20/LC_eff_EG20_tagWP80_probeWP80_EE_M_vs_EE_M_fitres.root", "READ")
print filein2.GetName()
c2= filein2.Get("ca")
print c2.GetName()
outfile.cd()
plist = c2.GetListOfPrimitives()
for pl in  plist: print pl.GetName()
histo3=c2.FindObject("h_data_Eff[l1_20_EE_M]").Clone()
histo3.SetName("h_data_Eff_l1_20_EE_M" )
curve3=c2.FindObject("cb_Norm[sc_et_EE_M]").Clone()
curve3.SetName("cb_Norm_sc_et_20_M_EE")
histo4=c2.FindObject("h_data2_Eff[l1_20_EE_M]" ).Clone()
histo4.SetName("h_data2_Eff_l1_20_EE_M" )
curve4=c2.FindObject("cb2_Norm[sc_et_EE_M]").Clone()
curve4.SetName("cb2_Norm_sc_et_20_M_EE")
curve4.Write()
curve3.Write()
histo3.Write()
histo4.Write()
canvas.cd()
histo3.Draw("SAMEP")
histo3.GetYaxis().SetTitle("Efficiency")
histo3.GetXaxis().SetTitle("E_{T} [GeV]")
histo3.GetXaxis().SetTitleOffset(1.2)
histo3.GetYaxis().SetTitleOffset(1.2)
for point in range(0, histo3.GetN()):
    histo3.SetPointEXlow(point, 0)
    histo3.SetPointEXhigh(point, 0)

curve3.Draw("SAME")
curve3.SetLineColor(1)
histo4.Draw("SAMEP")
histo4.GetYaxis().SetTitle("Efficiency")
histo4.GetXaxis().SetTitle("E_{T} [GeV]")
histo4.GetXaxis().SetTitleOffset(1.2)
histo4.GetYaxis().SetTitleOffset(1.2)
for point in range(0, histo4.GetN()):
    histo4.SetPointEXlow(point, 0)
    histo4.SetPointEXhigh(point, 0)

curve4.Draw("SAME")
curve4.SetLineColor(2)
print histo3.GetName()

histo3.Draw("SAMEP")
curve3.Draw("SAME")
curve3.SetLineColor(3)
histo4.Draw("SAMEP")
curve4.Draw("SAME")
curve4.SetLineColor(4)
histo3.SetLineColor(3)
histo3.SetMarkerStyle(20)
histo3.SetMarkerColor(3)
histo4.SetLineColor(4)
histo4.SetMarkerStyle(20)
histo4.SetMarkerColor(4)
leg2 = ROOT.TLegend(0.46, 0.40, 0.89, 0.25)

#leg2.AddEntry(None ,"","")
leg2.SetTextSize(0.034)
leg2.AddEntry(None, "ENDCAP", "")
leg2.AddEntry(histo3, "New Laser Corrections" , "lp")
leg2.AddEntry(histo4, "Old Laser Corrections" , "lp")


leg.Draw()
leg2.Draw()
outfile.cd()
canvas.Write()


if canvas.GetLogx()==1: 
    canvas.Print("plot_LC_2012.root")
    canvas.Print("plot_LC_2012.png")
    canvas.Print("plot_LC_2012.pdf")
else:
    canvas.Print("plot_LC_2012_noLog.root")
    canvas.Print("plot_LC_2012_noLog.png")
    canvas.Print("plot_LC_2012_noLog.pdf")

    

canvas.Clear()

outfile.Close()