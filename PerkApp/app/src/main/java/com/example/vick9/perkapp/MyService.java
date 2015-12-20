package com.example.vick9.perkapp;

import android.app.Service;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.IBinder;
import android.util.Log;

import com.perk.perksdk.PerkManager;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

/**
 * Created by vick9 on 20-12-2015.
 */
public class MyService extends Service {

    String key =   "b623ce13de3a04d8f145262253f7a4c94c64d7f3";
    String eventLike = "037f5fc74e11847a6c37e8e55ca9251d810065ea";
    public String TAG = MyService.class.getSimpleName();
    private MyThread mythread;
    public boolean isRunning = false;

    @Override
    public IBinder onBind(Intent arg0) {
        return null;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        Log.e(TAG, "onCreate");
        mythread  = new MyThread();
    }

    @Override
    public synchronized void onDestroy() {
        super.onDestroy();
        Log.d(TAG, "onDestroy");
        if(!isRunning){
            mythread.interrupt();
            mythread.stop();
        }
    }

    public MyService() {
        super();
    }

    @Override
    public synchronized void onStart(Intent intent, int startId) {
        super.onStart(intent, startId);
        Log.d(TAG, "onStart");
        if(!isRunning){
            mythread.start();
            isRunning = true;
        }
    }

    public void readWebPage(){
        SharedPreferences sharedPreferences = getApplicationContext().getSharedPreferences("myPrefs", MODE_PRIVATE);
        String id = sharedPreferences.getString("latest", "NULL");
        int likes = sharedPreferences.getInt("like",0);
        if(!id.equals("NULL")) {
            Log.e("not in",";ollol");
            String ip=sharedPreferences.getString("ip","192.168.1.22:5992");
            String url="http://"+ip+"/wait";
            HttpClient httpclient = new DefaultHttpClient();
            HttpPost httppost = new HttpPost(url);
            httppost.addHeader("object_id",id);
            try {
               HttpResponse response = httpclient.execute(httppost);
                String result = EntityUtils.toString(response.getEntity());
                int like = Integer.parseInt(result);
                if(like>likes){
                    PerkManager.trackEvent(MainActivity.self, key, eventLike, false, null);
                    sharedPreferences.edit().putInt("like",like);
                }

                /*else if(Integer.parseInt(response.toString())>likes){

                    PerkManager.trackEvent(MainActivity.self, key, eventLike, false, null);
                }*/

            } catch (ClientProtocolException e) {
                Log.e("Reqeust","Sent");

            } catch (IOException e) {
                Log.e("Reqeust","Sent");
            }
        }

    }

    class MyThread extends Thread{
        static final long DELAY = 3000;
        @Override
        public void run(){
            while(isRunning){
                Log.d(TAG,"Running");
                try {
                    readWebPage();
                    Thread.sleep(DELAY);
                } catch (InterruptedException e) {
                    isRunning = false;
                    e.printStackTrace();
                }
            }
        }

    }

}

