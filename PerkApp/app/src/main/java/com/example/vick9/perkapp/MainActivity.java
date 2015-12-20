package com.example.vick9.perkapp;

import android.app.Service;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.IBinder;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.Toast;


import com.google.android.gms.playlog.internal.LogEvent;
import com.perk.perksdk.PerkManager;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;

import java.io.IOException;

import me.dm7.barcodescanner.zxing.ZXingScannerView;


public class MainActivity extends AppCompatActivity {

    private static final String TAG = "QRCode";
    LinearLayout viewPerk,scanCode,enterId;
    String key =   "b623ce13de3a04d8f145262253f7a4c94c64d7f3";
    String eventLike = "037f5fc74e11847a6c37e8e55ca9251d810065ea";
    public static AppCompatActivity self;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        toolbar.setTitle("DineOut");
        viewPerk = (LinearLayout)findViewById(R.id.main_view_perk);
        scanCode = (LinearLayout)findViewById(R.id.main_scan_code);
        enterId = (LinearLayout)findViewById(R.id.main_enter_id);
        PerkManager.startSession(MainActivity.this, key);
self=this;
        viewPerk.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                PerkManager.showPortal(getBaseContext(), key);
            }
        });

        scanCode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getBaseContext(), ScannerActivity.class));
            }
        });
        setSupportActionBar(toolbar);
        startService(new Intent(MainActivity.this, MyService.class));
        Log.e(TAG, "onCreate:service started" );
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }


    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            startActivity(new Intent(getBaseContext(),Main2Activity.class));
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

}
