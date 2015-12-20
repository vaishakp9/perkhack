package com.example.vick9.perkapp;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.PointF;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import com.facebook.AccessToken;
import com.facebook.Profile;
import com.google.zxing.Result;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

import me.dm7.barcodescanner.zxing.ZXingScannerView;

public class ScannerActivity extends AppCompatActivity implements ZXingScannerView.ResultHandler  {
    private static final String TAG = "ORCode";
    public String temp = "Dominos,M3,Pizzas were awesome!";
    private ZXingScannerView mScannerView;
    String ip = "";
    @Override
    public void onCreate(Bundle state) {
        super.onCreate(state);
        mScannerView = new ZXingScannerView(this);   // Programmatically initialize the scanner view
        setContentView(mScannerView);                // Set the scanner view as the content view
    }

    @Override
    public void onResume() {
        super.onResume();
        mScannerView.setResultHandler(this); // Register ourselves as a handler for scan results.
        mScannerView.startCamera();          // Start camera on resume
    }

    @Override
    public void onPause() {
        super.onPause();
        mScannerView.stopCamera();           // Stop camera on pause
    }

    @Override
    public void handleResult(Result rawResult) {
        // Do something with the result here
        Log.v(TAG, rawResult.getText()); // Prints scan results
        Log.v(TAG, rawResult.getBarcodeFormat().toString());
        temp = rawResult.getText();
        new Send().execute();
        // Prints the scan format (qrcode, pdf417 etc.)

    }
    public class Send extends AsyncTask<Boolean,Boolean,Boolean>{

        @Override
        protected Boolean doInBackground(Boolean... params) {
            SharedPreferences sharedPreferences = getApplicationContext().getSharedPreferences("myPrefs",MODE_PRIVATE);
            ip=sharedPreferences.getString("ip","192.168.1.22:5992");
            String url="http://"+ip+"/resto";
            HttpClient httpclient = new DefaultHttpClient();
            HttpPost httppost = new HttpPost(url);
            httppost.addHeader("uid",temp);
            try {
                HttpResponse response = httpclient.execute(httppost);
                Log.e("Response",response.toString());
                if(response.toString().equals("NO")){
                    Toast.makeText(getBaseContext(),"Invalid Code",Toast.LENGTH_SHORT).show();

                }
                else {

                    Intent postIntent = new Intent(getBaseContext(),PostActivity.class);
                    String result = EntityUtils.toString(response.getEntity());
                    postIntent.putExtra("response",result);
                    startActivity(postIntent);
                    finish();
                }
            } catch (ClientProtocolException e) {

            } catch (IOException e) {

            }
            return null;
        }

        @Override
        protected void onPostExecute(Boolean aBoolean) {
            super.onPostExecute(aBoolean);
        }
    }
}