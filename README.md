# annotation_txt_to_xml

### This is sample code for txt to xml converter for python


##txt annotation file example
### first is number
### class x_min x_max y_min y_max
20
1 0 157 52 321  
1 28 166 82 299  
1 61 144 127 307  
1 127 168 179 295  
1 177 161 231 292  
1 223 165 270 281  
1 277 178 314 271  
1 314 168 353 266  
1 345 177 369 237  
1 370 180 402 258  
1 392 186 419 251  
1 432 180 458 244  
1 419 185 443 247  
1 475 189 496 240  
1 500 187 518 233  
1 218 177 242 236  
1 520 191 535 230  
1 448 184 471 242  
1 166 165 200 247  
1 273 182 286 207  

## After Converter
##xml annotation file example

\<annotatioin\>  
&nbsp;\<filename\>016986.jpg\</filename\>  
&nbsp;\<size\>  
    <width>549</width>  
    <height>362</height>  
    <depth>3</depth>  
  </size>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>0</xmin>  
      <ymin>157</ymin>  
      <xmax>52</xmax>  
      <ymax>321</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>28</xmin>  
      <ymin>166</ymin>  
      <xmax>82</xmax>  
      <ymax>299</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>61</xmin>  
      <ymin>144</ymin>  
      <xmax>127</xmax>  
      <ymax>307</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>127</xmin>  
      <ymin>168</ymin>  
      <xmax>179</xmax>  
      <ymax>295</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>177</xmin>  
      <ymin>161</ymin>  
      <xmax>231</xmax>  
      <ymax>292</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>223</xmin>  
      <ymin>165</ymin>  
      <xmax>270</xmax>  
      <ymax>281</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>277</xmin>  
      <ymin>178</ymin>  
      <xmax>314</xmax>  
      <ymax>271</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>314</xmin>  
      <ymin>168</ymin>  
      <xmax>353</xmax>  
      <ymax>266</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>345</xmin>  
      <ymin>177</ymin>  
      <xmax>369</xmax>  
      <ymax>237</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>370</xmin>  
      <ymin>180</ymin>  
      <xmax>402</xmax>  
      <ymax>258</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>392</xmin>  
      <ymin>186</ymin>  
      <xmax>419</xmax>  
      <ymax>251</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>432</xmin>  
      <ymin>180</ymin>  
      <xmax>458</xmax>  
      <ymax>244</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>419</xmin>  
      <ymin>185</ymin>  
      <xmax>443</xmax>  
      <ymax>247</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>475</xmin>  
      <ymin>189</ymin>  
      <xmax>496</xmax>  
      <ymax>240</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>500</xmin>  
      <ymin>187</ymin>  
      <xmax>518</xmax>  
      <ymax>233</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>218</xmin>  
      <ymin>177</ymin>  
      <xmax>242</xmax>  
      <ymax>236</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>520</xmin>  
      <ymin>191</ymin>  
      <xmax>535</xmax>  
      <ymax>230</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>448</xmin>  
      <ymin>184</ymin>  
      <xmax>471</xmax>  
      <ymax>242</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>166</xmin>  
      <ymin>165</ymin>  
      <xmax>200</xmax>  
      <ymax>247</ymax>  
    </bndbox>  
  </object>  
  <object>  
    <name>person</name>  
    <bndbox>  
      <xmin>273</xmin>  
      <ymin>182</ymin>  
      <xmax>286</xmax>  
      <ymax>207</ymax>  
    </bndbox>  
  </object>  
</annotatioin>  
